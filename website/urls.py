from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("ecosystem/", views.ecosystem, name="ecosystem"),
    path("who-we-serve/", views.who_we_serve, name="who_we_serve"),
    path("approach/", views.approach, name="approach"),
    path("why-lyra/", views.why_lyra, name="why_lyra"),
    path("contact/", views.contact, name="contact"),
]
