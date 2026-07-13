from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("ecosystem/", views.ecosystem, name="ecosystem"),
    path("ai-agora/", views.ai_agora, name="ai_agora"),
    path("agora/go/<slug:slug>/", views.agora_referral_redirect, name="agora_referral_redirect"),
    path("agora/webhook/enrollment/", views.agora_referral_webhook, name="agora_referral_webhook"),
    path("who-we-serve/", views.who_we_serve, name="who_we_serve"),
    path("approach/", views.approach, name="approach"),
    path("why-lyra/", views.why_lyra, name="why_lyra"),
    path("contact/", views.contact, name="contact"),
]
