from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("free-counselling/", views.counselling, name="counselling"),
    path("thank-you/", views.thank_you, name="thank_you"),
    path("university-shortlisting/", views.counselling, {"variant": "shortlisting"}, name="shortlisting"),
    path("about-us/", views.about, name="about"),
    path("about-us/team/", views.team, name="team"),
    path("about-us/partners/", views.partners, name="partners"),
    path("about-us/testimonials/", views.testimonials, name="testimonials"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq_page, name="faq"),
    path("sitemap/", views.sitemap_page, name="sitemap"),
    path("<slug:slug>/", views.legal_page, name="page"),
]
