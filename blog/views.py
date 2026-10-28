from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.db.models import Count, F, Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.models import Section
from core.views import hero_for

from .models import BlogCategory, Post, Subscriber


def _sidebar():
    published = Post.objects.published()
    return {
        "categories": BlogCategory.objects.filter(is_active=True).annotate(
            n=Count("posts", filter=Q(posts__in=published))
        ),
        "featured": published.filter(is_featured=True).first(),
    }


def post_list(request, category_slug=None):
    posts = Post.objects.published().select_related("category")
    category = None
    if category_slug:
        category = get_object_or_404(BlogCategory, slug=category_slug, is_active=True)
        posts = posts.filter(category=category)
    q = request.GET.get("q", "").strip()
    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(excerpt__icontains=q) | Q(content__icontains=q))
    page = Paginator(posts, 9).get_page(request.GET.get("page"))
    return render(
        request,
        "blog/list.html",
        {
            "hero": hero_for("blog"),
            "sections": Section.for_page("blog"),
            "page_obj": page,
            "current_category": category,
            "q": q,
            **_sidebar(),
        },
    )


def post_detail(request, slug):
    post = get_object_or_404(Post.objects.published().select_related("category", "author"), slug=slug)
    Post.objects.filter(pk=post.pk).update(views=F("views") + 1)
    related = Post.objects.published().filter(category=post.category).exclude(pk=post.pk)[:3]
    return render(
        request,
        "blog/detail.html",
        {"post": post, "related": related, "sections": Section.for_page("blog"), **_sidebar()},
    )


@require_POST
def subscribe(request):
    email = request.POST.get("email", "").strip().lower()
    ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"
    try:
        validate_email(email)
    except ValidationError:
        if ajax:
            return JsonResponse({"ok": False, "message": "Please enter a valid email address."}, status=400)
        messages.error(request, "Please enter a valid email address.")
        return redirect("blog:list")
    Subscriber.objects.get_or_create(email=email)
    msg = "You're subscribed! Watch your inbox for study abroad updates."
    if ajax:
        return JsonResponse({"ok": True, "message": msg})
    messages.success(request, msg)
    return redirect("blog:list")
