"""
Two separate admin panels:

* Super Admin  (/superadmin/) – superusers only. Manages everything: users & roles,
  enquiries/leads, subscribers and all website content.
* Website Admin (/cms/)       – members of the "Website Admin" group. A WordPress-style
  content panel limited to website content (pages, destinations, blog, FAQs ...).
"""

from datetime import timedelta

from django.conf import settings
from django.contrib.admin import AdminSite
from django.db.models import Count
from django.http import JsonResponse
from django.urls import path, reverse
from django.utils import timezone
from django.utils.timesince import timesince


class BrandedAdminSite(AdminSite):
    site_title = "UniLeap Overseas"
    site_url = "/"
    enable_nav_sidebar = True
    panel_label = ""

    def each_context(self, request):
        context = super().each_context(request)
        context["panel_label"] = self.panel_label
        context["panel_name"] = self.name
        return context


class SuperAdminSite(BrandedAdminSite):
    site_header = "UniLeap Super Admin"
    index_title = "Super Admin Dashboard"
    panel_label = "Super Admin"
    index_template = "admin/super_index.html"

    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser

    def get_urls(self):
        urls = [path("live/", self.admin_view(self.live_feed), name="live_feed")]
        return urls + super().get_urls()

    def index(self, request, extra_context=None):
        from blog.models import Post, Subscriber
        from catalog.models import Course, Destination, University
        from django.contrib.auth import get_user_model
        from leads.models import Enquiry

        User = get_user_model()
        now = timezone.now()
        today = timezone.localdate()
        enquiries = Enquiry.objects.all()
        extra_context = {
            **(extra_context or {}),
            "stats": {
                "enquiries_total": enquiries.count(),
                "enquiries_new": enquiries.filter(status="new").count(),
                "enquiries_today": enquiries.filter(created_at__date=today).count(),
                "enquiries_week": enquiries.filter(created_at__gte=now - timedelta(days=7)).count(),
                "converted": enquiries.filter(status="converted").count(),
                "destinations": Destination.objects.count(),
                "universities": University.objects.count(),
                "courses": Course.objects.count(),
                "posts": Post.objects.published().count(),
                "drafts": Post.objects.filter(status=Post.DRAFT).count(),
                "subscribers": Subscriber.objects.count(),
                "superadmins": User.objects.filter(is_superuser=True, is_active=True).count(),
                "website_admins": User.objects.filter(
                    groups__name=settings.WEBSITE_ADMIN_GROUP, is_active=True, is_superuser=False
                ).count(),
            },
            "by_destination": enquiries.values("destination").annotate(n=Count("id")).order_by("-n")[:6],
            "by_status": [
                {**row, "label": dict(Enquiry.STATUSES).get(row["status"], row["status"])}
                for row in enquiries.values("status").annotate(n=Count("id")).order_by("-n")
            ],
        }
        return super().index(request, extra_context)

    def live_feed(self, request):
        """JSON feed polled by the dashboard for real-time enquiry updates."""
        from leads.models import Enquiry

        since = int(request.GET.get("since") or 0)
        latest = Enquiry.objects.order_by("-id")
        items = latest.filter(id__gt=since)[:20] if since else latest[:10]
        return JsonResponse(
            {
                "last_id": latest.values_list("id", flat=True).first() or 0,
                "counts": {
                    "new": Enquiry.objects.filter(status="new").count(),
                    "today": Enquiry.objects.filter(created_at__date=timezone.localdate()).count(),
                    "total": Enquiry.objects.count(),
                },
                "items": [
                    {
                        "id": e.id,
                        "name": e.full_name,
                        "email": e.email,
                        "phone": e.phone,
                        "destination": e.destination,
                        "intake": e.intake,
                        "source": e.source,
                        "status": e.get_status_display(),
                        "status_key": e.status,
                        "ago": timesince(e.created_at) + " ago",
                        "url": reverse(f"{self.name}:leads_enquiry_change", args=[e.id]),
                    }
                    for e in items
                ],
            }
        )


class WebsiteAdminSite(BrandedAdminSite):
    site_header = "UniLeap Website Admin"
    index_title = "Website Content"
    panel_label = "Website Admin"
    index_template = "admin/cms_index.html"

    def has_permission(self, request):
        user = request.user
        return (
            user.is_active
            and user.is_staff
            and (user.is_superuser or user.groups.filter(name=settings.WEBSITE_ADMIN_GROUP).exists())
        )

    def index(self, request, extra_context=None):
        from blog.models import Post
        from catalog.models import Course, Destination, University
        from core.models import FAQ

        extra_context = {
            **(extra_context or {}),
            "counts": {
                "destinations": Destination.objects.count(),
                "universities": University.objects.count(),
                "courses": Course.objects.count(),
                "posts": Post.objects.published().count(),
                "drafts": Post.objects.filter(status=Post.DRAFT).count(),
                "faqs": FAQ.objects.count(),
            },
            "recent_posts": Post.objects.select_related("category").order_by("-updated_at")[:6],
        }
        return super().index(request, extra_context)


super_admin_site = SuperAdminSite(name="superadmin")
website_admin_site = WebsiteAdminSite(name="cms")

BOTH_SITES = (super_admin_site, website_admin_site)
SUPER_ONLY = (super_admin_site,)


def register(*models, sites=BOTH_SITES):
    """Like @admin.register, but registers the ModelAdmin on several admin sites."""

    def wrapper(admin_class):
        for site in sites:
            site.register(models, admin_class)
        return admin_class

    return wrapper
