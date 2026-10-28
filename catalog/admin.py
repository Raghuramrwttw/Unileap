from django.contrib import admin

from core.admin import IconMixin, OrderableAdmin, ThumbnailMixin
from unileap.admin_sites import register

from .models import Course, CourseCategory, Destination, DestinationHighlight, University


class DestinationHighlightInline(admin.TabularInline):
    model = DestinationHighlight
    extra = 0
    fields = ("icon", "text", "order", "is_active")


@register(Destination)
class DestinationAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("name", "full_name", "thumb", "show_on_home", "order", "is_active")
    list_editable = ("order", "is_active", "show_on_home")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [DestinationHighlightInline]
    fieldsets = (
        (None, {"fields": ("name", "full_name", "slug", "country_code", ("image", "image_url"))}),
        ("Card text", {"fields": ("short_description", "tagline", "summary")}),
        ("Detail page", {"fields": ("description",)}),
        (
            "Comparison data",
            {"fields": ("currency", "tuition_fees", "post_study_work", "cost_of_living", "pr_options", "popular_intakes")},
        ),
        ("Display", {"fields": ("show_on_home", "order", "is_active")}),
    )


@register(CourseCategory)
class CourseCategoryAdmin(OrderableAdmin):
    list_display = ("name", "icon_preview", "order", "is_active")
    prepopulated_fields = {"slug": ("name",)}


class CourseInline(admin.TabularInline):
    model = Course
    extra = 0
    fields = ("name", "category", "level", "duration", "intakes", "tuition_fee", "is_popular", "is_active")


@register(University)
class UniversityAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("name", "destination", "city", "thumb", "is_top", "order", "is_active")
    list_editable = ("is_top", "order", "is_active")
    list_filter = ("destination", "institution_type", "is_top", "is_active")
    search_fields = ("name", "city")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CourseInline]
    fields = (
        ("name", "slug"),
        ("destination", "city"),
        ("institution_type", "established"),
        "ranking",
        ("image", "image_url"),
        "description",
        "website",
        ("is_top", "order", "is_active"),
    )


@register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "university", "category", "level", "intakes", "tuition_fee", "is_popular", "is_active")
    list_editable = ("is_popular", "is_active")
    list_filter = ("level", "category", "university__destination", "is_popular")
    search_fields = ("name", "university__name")
    autocomplete_fields = ("university",)
    list_select_related = ("university", "category")
