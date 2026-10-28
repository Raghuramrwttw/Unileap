from django.contrib import admin

from core.admin import OrderableAdmin, ThumbnailMixin
from unileap.admin_sites import SUPER_ONLY, register

from .models import BlogCategory, Post, Subscriber


@register(BlogCategory)
class BlogCategoryAdmin(OrderableAdmin):
    list_display = ("name", "icon_preview", "post_count", "order", "is_active")
    prepopulated_fields = {"slug": ("name",)}

    @admin.display(description="Posts")
    def post_count(self, obj):
        return obj.posts.count()


@register(Post)
class PostAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("title", "category", "thumb", "status", "is_featured", "published_at", "views")
    list_filter = ("status", "category", "is_featured")
    list_editable = ("status", "is_featured")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "published_at"
    actions = ["publish", "unpublish"]
    fieldsets = (
        (None, {"fields": ("title", "slug", "category", ("tag", "tag_color"))}),
        ("Content", {"fields": ("excerpt", "content", ("image", "image_url"))}),
        ("Publishing", {"fields": (("status", "published_at"), "is_featured", "meta_description")}),
    )

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)

    @admin.action(description="Publish selected posts")
    def publish(self, request, queryset):
        queryset.update(status=Post.PUBLISHED)

    @admin.action(description="Move selected posts to draft")
    def unpublish(self, request, queryset):
        queryset.update(status=Post.DRAFT)


@register(Subscriber, sites=SUPER_ONLY)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
    date_hierarchy = "created_at"
