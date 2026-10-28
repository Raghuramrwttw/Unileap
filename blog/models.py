from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone

from core.fields import RichTextField
from core.models import ICON_HELP, Orderable, WithImage


class BlogCategory(Orderable):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=60, help_text=ICON_HELP)

    class Meta(Orderable.Meta):
        verbose_name_plural = "Blog categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blog:category", args=[self.slug])


class PostQuerySet(models.QuerySet):
    def published(self):
        return self.filter(status=Post.PUBLISHED, published_at__lte=timezone.now())


class Post(WithImage):
    DRAFT, PUBLISHED = "draft", "published"
    STATUSES = [(DRAFT, "Draft"), (PUBLISHED, "Published")]
    TAG_COLORS = [
        ("blue", "Blue"),
        ("red", "Red"),
        ("green", "Green"),
        ("orange", "Orange"),
        ("yellow", "Yellow"),
        ("purple", "Purple"),
        ("pink", "Pink"),
        ("teal", "Teal"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=220)
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT, related_name="posts")
    tag = models.CharField(max_length=30, blank=True, help_text='Label on the image, e.g. "UK" or "VISA".')
    tag_color = models.CharField(max_length=10, choices=TAG_COLORS, default="blue")
    excerpt = models.TextField(max_length=400)
    content = RichTextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=10, choices=STATUSES, default=DRAFT, db_index=True)
    is_featured = models.BooleanField(default=False, help_text="Show in the Featured Post box.")
    published_at = models.DateTimeField(default=timezone.now, help_text="Set a future date to schedule the post.")
    meta_description = models.CharField(max_length=300, blank=True)
    views = models.PositiveIntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", args=[self.slug])


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Newsletter subscriber"

    def __str__(self):
        return self.email
