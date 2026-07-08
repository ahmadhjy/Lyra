from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import render

from . import content


def _nav_context(active):
    return {
        "nav_items": content.NAV,
        "active_page": active,
    }


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
    ctx = {**_nav_context("contact"), **content.CONTACT}
    ctx["contact_email"] = settings.CONTACT_EMAIL
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
