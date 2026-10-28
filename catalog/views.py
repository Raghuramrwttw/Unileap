from django.core.paginator import Paginator
from django.db.models import Count, Max, Min, Prefetch, Q
from django.shortcuts import get_object_or_404, render

from core.models import FeatureItem, Section
from core.views import hero_for

from .models import INTAKE_MONTHS as INTAKE_FILTERS, Course, CourseCategory, Destination, University

SORTS = {
    "popular": ("order", "name"),
    "name": ("name",),
    "oldest": ("established",),
    "fee_low": ("min_fee",),
}


def destinations(request):
    return render(
        request,
        "catalog/destinations.html",
        {
            "hero": hero_for("destinations"),
            "sections": Section.for_page("destinations"),
            "destinations": Destination.objects.filter(is_active=True).prefetch_related("highlights"),
            "compare_factors": FeatureItem.objects.filter(group="compare_factors", is_active=True),
            "why_items": FeatureItem.objects.filter(group="destinations_why", is_active=True),
        },
    )


def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug, is_active=True)
    universities = (
        destination.universities.filter(is_active=True)
        .select_related("destination")
        .prefetch_related(
            Prefetch("courses", queryset=Course.objects.filter(is_active=True), to_attr="matching_courses")
        )
    )
    return render(
        request,
        "catalog/destination_detail.html",
        {
            "destination": destination,
            "universities": universities[:6],
            "university_count": universities.count(),
            "others": Destination.objects.filter(is_active=True).exclude(pk=destination.pk),
        },
    )


def compare(request):
    return render(
        request,
        "catalog/compare.html",
        {"destinations": Destination.objects.filter(is_active=True), "rows": COMPARE_ROWS},
    )


COMPARE_ROWS = [
    ("Tuition fees (per year)", "tuition_fees", "fa-solid fa-graduation-cap"),
    ("Post-study work", "post_study_work", "fa-solid fa-briefcase"),
    ("Cost of living (per year)", "cost_of_living", "fa-solid fa-house"),
    ("PR options", "pr_options", "fa-solid fa-users"),
    ("Popular intakes", "popular_intakes", "fa-solid fa-calendar-days"),
]


def universities(request, top_only=False):
    """University & course search with sidebar filters (destination, level, category, intake, fee)."""
    params = request.GET
    selected = {
        "destination": params.getlist("destination"),
        "level": params.getlist("level"),
        "category": params.getlist("category"),
        "intake": params.getlist("intake"),
    }
    q = params.get("q", "").strip()
    fee_max = params.get("fee_max", "").strip()

    courses = Course.objects.filter(is_active=True, university__is_active=True)
    if selected["level"]:
        courses = courses.filter(level__in=selected["level"])
    if selected["category"]:
        courses = courses.filter(category__slug__in=selected["category"])
    if selected["intake"]:
        intake_q = Q()
        for intake in selected["intake"]:
            intake_q |= Q(intakes__icontains=intake)
        courses = courses.filter(intake_q)
    if fee_max.isdigit():
        courses = courses.filter(tuition_fee__lte=int(fee_max))
    if q:
        courses = courses.filter(Q(name__icontains=q) | Q(university__name__icontains=q))

    unis = University.objects.filter(is_active=True)
    if top_only:
        unis = unis.filter(is_top=True)
    if selected["destination"]:
        unis = unis.filter(destination__slug__in=selected["destination"])
    course_filters_active = any(selected[k] for k in ("level", "category", "intake")) or fee_max.isdigit() or q
    if course_filters_active:
        unis = unis.filter(id__in=courses.values("university_id"))
    matching_courses = courses.filter(university__in=unis).count()
    unis = (
        unis.select_related("destination")
        .annotate(min_fee=Min("courses__tuition_fee"), max_fee=Max("courses__tuition_fee"))
        .prefetch_related(Prefetch("courses", queryset=courses.order_by("-is_popular", "order"), to_attr="matching_courses"))
    )
    sort = params.get("sort", "popular")
    unis = unis.order_by(*SORTS.get(sort, SORTS["popular"]))

    page = Paginator(unis, 9).get_page(params.get("page"))

    return render(
        request,
        "catalog/universities.html",
        {
            "hero": hero_for("universities"),
            "help": Section.objects.filter(key="universities.help").first(),
            "help_points": FeatureItem.objects.filter(group="universities_help", is_active=True),
            "page_obj": page,
            "total_unis": page.paginator.count,
            "total_courses": matching_courses,
            "all_destinations": Destination.objects.filter(is_active=True),
            "all_categories": CourseCategory.objects.filter(is_active=True),
            "levels": Course.LEVELS,
            "intakes": INTAKE_FILTERS,
            "selected": selected,
            "q": q,
            "fee_max": fee_max,
            "sort": sort,
            "top_only": top_only,
        },
    )


def top_universities(request):
    return universities(request, top_only=True)


def university_detail(request, slug):
    university = get_object_or_404(University.objects.select_related("destination"), slug=slug, is_active=True)
    courses = university.courses.filter(is_active=True).select_related("category")
    return render(
        request,
        "catalog/university_detail.html",
        {
            "university": university,
            "courses": courses,
            "related": University.objects.filter(destination=university.destination, is_active=True).exclude(pk=university.pk)[:3],
        },
    )


def courses(request, popular_only=False):
    qs = Course.objects.filter(is_active=True, university__is_active=True).select_related(
        "university", "university__destination", "category"
    )
    if popular_only:
        qs = qs.filter(is_popular=True)
    category = request.GET.get("category")
    level = request.GET.get("level")
    destination = request.GET.get("destination")
    intake = request.GET.get("intake")
    q = request.GET.get("q", "").strip()
    if category:
        qs = qs.filter(category__slug=category)
    if level:
        qs = qs.filter(level=level)
    if destination:
        qs = qs.filter(university__destination__slug=destination)
    if intake:
        qs = qs.filter(intakes__icontains=intake)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(university__name__icontains=q))
    page = Paginator(qs.order_by("category__order", "name"), 12).get_page(request.GET.get("page"))
    return render(
        request,
        "catalog/courses.html",
        {
            "page_obj": page,
            "categories": CourseCategory.objects.filter(is_active=True).annotate(n=Count("courses")),
            "levels": Course.LEVELS,
            "current_category": category,
            "current_level": level,
            "current_destination": Destination.objects.filter(slug=destination).first() if destination else None,
            "current_intake": intake,
            "q": q,
            "popular_only": popular_only,
        },
    )


def popular_courses(request):
    return courses(request, popular_only=True)
