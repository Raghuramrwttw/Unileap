from django.shortcuts import get_object_or_404, redirect, render

from blog.models import BlogCategory, Post
from catalog.models import Course, CourseCategory, Destination
from loans.models import Lender

from .models import FAQ, FeatureItem, LegalPage, PageHero, Partner, ProcessStep, Section, Service, Stat, TeamMember, Testimonial


def hero_for(page):
    return PageHero.objects.filter(page=page).prefetch_related("features").first()


def features(group):
    return FeatureItem.objects.filter(group=group, is_active=True)


def faqs(group):
    return FAQ.objects.filter(group=group, is_active=True)


def home(request):
    return render(
        request,
        "core/home.html",
        {
            "hero": hero_for("home"),
            "sections": Section.for_page("home"),
            "destinations": Destination.objects.filter(is_active=True, show_on_home=True),
            "categories": CourseCategory.objects.filter(is_active=True),
            "services": Service.objects.filter(is_active=True),
            "steps": ProcessStep.objects.filter(group="home_journey", is_active=True),
            "why_items": features("home_why"),
            "trending": features("home_trending"),
            "stats": Stat.objects.filter(is_active=True),
            "testimonials": Testimonial.objects.filter(is_active=True)[:4],
            "posts": Post.objects.published().select_related("category")[:3],
            "faqs": faqs("home")[:6],
            "search_destinations": Destination.objects.filter(is_active=True),
            "search_levels": Course.LEVELS,
        },
    )


def about(request):
    return render(
        request,
        "core/about.html",
        {
            "hero": hero_for("about"),
            "sections": Section.for_page("about"),
            "destinations": Destination.objects.filter(is_active=True),
            "stats": Stat.objects.filter(is_active=True),
            "foundation": features("about_foundation"),
            "values": features("about_values"),
            "why_items": features("about_why"),
        },
    )


def team(request):
    return render(
        request,
        "core/team.html",
        {"section": Section.objects.filter(key="team.intro").first(), "members": TeamMember.objects.filter(is_active=True)},
    )


def partners(request):
    return render(
        request,
        "core/partners.html",
        {
            "section": Section.objects.filter(key="partners.intro").first(),
            "partners": Partner.objects.filter(is_active=True),
            "lenders": Lender.objects.filter(is_active=True),
        },
    )


def testimonials(request):
    return render(
        request,
        "core/testimonials.html",
        {
            "section": Section.objects.filter(key="testimonials.intro").first(),
            "testimonials": Testimonial.objects.filter(is_active=True),
        },
    )


def contact(request):
    return render(
        request,
        "core/contact.html",
        {
            "hero": hero_for("contact"),
            "sections": Section.for_page("contact"),
            "online_points": features("contact_online"),
            "cta_points": features("contact_cta"),
            "faqs": faqs("contact"),
        },
    )


def counselling(request, variant="counselling"):
    return render(
        request,
        "core/counselling.html",
        {
            "hero": hero_for("counselling"),
            "variant": variant,
            "steps": ProcessStep.objects.filter(group="home_journey", is_active=True),
            "services": Service.objects.filter(is_active=True),
        },
    )


def thank_you(request):
    """Shown after an enquiry is submitted. Direct visits go to the home page."""
    first_name = request.session.get("enquiry_submitted")
    if not first_name:
        return redirect("core:home")
    return render(
        request,
        "core/thank_you.html",
        {"first_name": first_name, "sections": Section.for_page("thanks"), "steps": features("thanks_next")},
    )


def faq_page(request):
    groups = [(label, faqs(key)) for key, label in FAQ.GROUPS]
    return render(request, "core/faq.html", {"groups": [(label, items) for label, items in groups if items]})


def sitemap_page(request):
    return render(
        request,
        "core/sitemap.html",
        {
            "destinations": Destination.objects.filter(is_active=True),
            "categories": CourseCategory.objects.filter(is_active=True),
            "blog_categories": BlogCategory.objects.filter(is_active=True),
            "pages": LegalPage.objects.filter(is_active=True),
            "recent_posts": Post.objects.published()[:8],
        },
    )


def legal_page(request, slug):
    page = get_object_or_404(LegalPage, slug=slug, is_active=True)
    return render(request, "core/legal.html", {"page": page})


def page_not_found(request, exception=None):
    return render(request, "404.html", status=404)


def server_error(request):
    return render(request, "500.html", status=500)
