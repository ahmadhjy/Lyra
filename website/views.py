import json
import uuid
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl

from django.conf import settings
from django.http import Http404, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from . import content
from .agora_courses import AGORA, COURSES, course_by_slug, matrix_course_url
from .models import AgoraReferralClick, AgoraReferralConversion


def _nav_context(active):
    return {
        "nav_items": content.NAV,
        "active_page": active,
    }


def _client_ip(request):
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def _append_tracking_params(url, params):
    parts = urlparse(url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query.update(params)
    return urlunparse(parts._replace(query=urlencode(query)))


def home(request):
    return render(
        request,
        "website/home.html",
        {**_nav_context("home"), **content.HOME},
    )


def about(request):
    return render(
        request,
        "website/page.html",
        {**_nav_context("about"), "page": content.ABOUT},
    )


def ecosystem(request):
    return render(
        request,
        "website/page.html",
        {**_nav_context("ecosystem"), "page": content.ECOSYSTEM},
    )


def ai_agora(request):
    return render(
        request,
        "website/ai_agora.html",
        {
            **_nav_context("ai_agora"),
            **AGORA,
            "courses": COURSES,
        },
    )


def agora_referral_redirect(request, slug):
    course = course_by_slug(slug)
    if not course:
        raise Http404("Course not found")

    ref_id = uuid.uuid4()
    destination = matrix_course_url(slug)
    tracking = {
        "lyra_ref": str(ref_id),
        "utm_source": "lyra",
        "utm_medium": "referral",
        "utm_campaign": "ai-agora",
        "utm_content": slug,
    }
    destination = _append_tracking_params(destination, tracking)

    if not request.session.session_key:
        request.session.save()

    AgoraReferralClick.objects.create(
        ref_id=ref_id,
        course_slug=slug,
        course_title=course["title"],
        destination_url=destination,
        ip_address=_client_ip(request),
        user_agent=request.META.get("HTTP_USER_AGENT", "")[:1000],
        session_key=request.session.session_key or "",
    )

    return redirect(destination)


@csrf_exempt
@require_POST
def agora_referral_webhook(request):
    secret = getattr(settings, "AGORA_WEBHOOK_SECRET", "")
    if not secret:
        return JsonResponse({"error": "Webhook not configured"}, status=503)

    provided = request.headers.get("X-Lyra-Webhook-Secret", "")
    if provided != secret:
        return JsonResponse({"error": "Unauthorized"}, status=401)

    try:
        payload = json.loads(request.body.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    lyra_ref = str(payload.get("lyra_ref", "")).strip()
    if not lyra_ref:
        return JsonResponse({"error": "lyra_ref is required"}, status=400)

    click = None
    try:
        click = AgoraReferralClick.objects.get(ref_id=lyra_ref)
    except (AgoraReferralClick.DoesNotExist, ValueError):
        click = None

    conversion = AgoraReferralConversion.objects.create(
        click=click,
        lyra_ref=lyra_ref,
        course_slug=str(payload.get("course_slug", "")).strip(),
        event_type=str(payload.get("event_type", "enrollment")).strip() or "enrollment",
        payload=payload,
    )

    return JsonResponse(
        {
            "ok": True,
            "conversion_id": conversion.id,
            "matched_click": bool(click),
        }
    )


def who_we_serve(request):
    return render(
        request,
        "website/page.html",
        {**_nav_context("who_we_serve"), "page": content.WHO_WE_SERVE},
    )


def approach(request):
    return render(
        request,
        "website/page.html",
        {**_nav_context("approach"), "page": content.APPROACH},
    )


def why_lyra(request):
    return render(
        request,
        "website/page.html",
        {**_nav_context("why_lyra"), "page": content.WHY_LYRA},
    )


def contact(request):
    from django.core.mail import EmailMessage

    ctx = {**_nav_context("contact"), **content.CONTACT}
    ctx["contact_email"] = getattr(settings, "CONTACT_EMAIL", "info@lyraaiqat.com")
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        organization = request.POST.get("organization", "").strip()
        message = request.POST.get("message", "").strip()

        body = (
            "New contact form submission from lyraaiqat.com\n\n"
            f"Name: {name or '—'}\n"
            f"Email: {email or '—'}\n"
            f"Organization: {organization or '—'}\n\n"
            f"Message:\n{message or '—'}\n"
        )

        EmailMessage(
            subject=f"[LYRA] New inquiry from {name or 'website visitor'}",
            body=body,
            to=[settings.CONTACT_EMAIL],
            reply_to=[email] if email else None,
        ).send(fail_silently=True)

        ctx["form_sent"] = True
    return render(request, "website/contact.html", ctx)
