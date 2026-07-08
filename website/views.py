from django.conf import settings
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
    ctx["contact_email"] = getattr(settings, "CONTACT_EMAIL", "info@lyraaiqat.com")
    # Form is UI-only for now — email delivery stays disabled until
    # the client provides mailbox / SMTP access for info@lyraaiqat.com.
    if request.method == "POST":
        ctx["form_sent"] = True
    return render(request, "website/contact.html", ctx)
