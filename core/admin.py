from django.conf import settings
from django.contrib import admin, messages
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.html import format_html

from unileap.admin_sites import SUPER_ONLY, register

from .models import (
    FAQ,
    FeatureItem,
    HeroFeature,
    LegalPage,
    PageHero,
    Partner,
    ProcessStep,
    Section,
    Service,
    SiteSettings,
    Stat,
    TeamMember,
    Testimonial,
)


class ThumbnailMixin:
    @admin.display(description="Image")
    def thumb(self, obj):
        src = getattr(obj, "image_src", "")
        if not src:
            return "—"
        return format_html('<img src="{}" style="height:42px;width:64px;object-fit:cover;border-radius:6px">', src)


class IconMixin:
    @admin.display(description="Icon")
    def icon_preview(self, obj):
        if not obj.icon:
            return "—"
        return format_html('<i class="{}" style="font-size:18px;color:#1f5fe0"></i>', obj.icon)


class OrderableAdmin(IconMixin, admin.ModelAdmin):
    list_editable = ("order", "is_active")
    list_filter = ("is_active",)


@register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Branding", {"fields": ("site_name", "tagline", "logo", "meta_description")}),
        ("Contact details", {"fields": ("phone", "whatsapp", "email", "email_note", "city", "address", "hours", "closed_note")}),
        ("Social media", {"fields": ("facebook_url", "instagram_url", "linkedin_url", "youtube_url")}),
        ("Map & office", {"fields": ("map_embed_url", "office_image_url")}),
        ("Footer & call to action", {"fields": ("footer_about", "cta_title", "cta_subtitle", "cta_image_url", "privacy_note")}),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        obj = SiteSettings.load()
        return redirect(reverse(f"{self.admin_site.name}:core_sitesettings_change", args=[obj.pk]))


class HeroFeatureInline(admin.TabularInline):
    model = HeroFeature
    extra = 0
    fields = ("icon", "label", "order", "is_active")


@register(PageHero)
class PageHeroAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("__str__", "title", "thumb", "show_counselling_form")
    inlines = [HeroFeatureInline]
    fields = ("page", "eyebrow", "title", "subtitle", "script_text", ("image", "image_url"), "show_counselling_form")


@register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("__str__", "title", "eyebrow")
    search_fields = ("title", "subtitle", "key")
    fields = (
        "key",
        "eyebrow",
        "title",
        "subtitle",
        "body",
        ("button_text", "button_link"),
        "script_text",
        ("image", "image_url"),
    )


@register(FeatureItem)
class FeatureItemAdmin(OrderableAdmin):
    list_display = ("title", "icon_preview", "group", "order", "is_active")
    list_filter = ("group", "is_active")
    search_fields = ("title", "description")


@register(Service)
class ServiceAdmin(OrderableAdmin):
    list_display = ("title", "icon_preview", "order", "is_active")


@register(ProcessStep)
class ProcessStepAdmin(OrderableAdmin):
    list_display = ("title", "icon_preview", "group", "order", "is_active")
    list_filter = ("group",)


@register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "group", "order", "is_active")
    list_editable = ("order", "is_active")
    list_filter = ("group", "is_active")
    search_fields = ("question", "answer")


@register(Stat)
class StatAdmin(OrderableAdmin):
    list_display = ("value", "label", "icon_preview", "order", "is_active")


@register(TeamMember)
class TeamMemberAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("name", "role", "thumb", "order", "is_active")
    list_editable = ("order", "is_active")


@register(Partner)
class PartnerAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("name", "thumb", "website", "order", "is_active")
    list_editable = ("order", "is_active")


@register(Testimonial)
class TestimonialAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("name", "detail", "rating", "thumb", "order", "is_active")
    list_editable = ("order", "is_active")


@register(LegalPage)
class LegalPageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "show_in_footer", "is_active", "updated_at")
    prepopulated_fields = {"slug": ("title",)}


# ---- Users & roles (Super Admin only) -------------------------------------------------


@register(User, sites=SUPER_ONLY)
class UnileapUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "role", "is_active", "last_login")
    list_filter = ("is_superuser", "is_active", "groups")
    actions = ["make_website_admin", "remove_website_admin"]

    @admin.display(description="Role")
    def role(self, obj):
        if obj.is_superuser:
            return format_html('<span class="role-badge role-super">{}</span>', "Super Admin")
        if obj.groups.filter(name=settings.WEBSITE_ADMIN_GROUP).exists():
            return format_html('<span class="role-badge role-web">{}</span>', "Website Admin")
        return "—"

    @admin.action(description="Make selected users Website Admins")
    def make_website_admin(self, request, queryset):
        group, _ = Group.objects.get_or_create(name=settings.WEBSITE_ADMIN_GROUP)
        for user in queryset:
            user.is_staff = True
            user.save(update_fields=["is_staff"])
            user.groups.add(group)
        self.message_user(request, f"{queryset.count()} user(s) can now use the Website Admin panel.", messages.SUCCESS)

    @admin.action(description="Remove Website Admin role")
    def remove_website_admin(self, request, queryset):
        group = Group.objects.filter(name=settings.WEBSITE_ADMIN_GROUP).first()
        if group:
            for user in queryset:
                user.groups.remove(group)
        self.message_user(request, "Website Admin role removed.", messages.SUCCESS)


register(Group, sites=SUPER_ONLY)(GroupAdmin)
