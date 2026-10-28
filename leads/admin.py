import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html

from unileap.admin_sites import SUPER_ONLY, register

from .models import Enquiry

STATUS_COLORS = {
    "new": "#1f5fe0",
    "contacted": "#7c3aed",
    "in_progress": "#d97706",
    "converted": "#16a34a",
    "closed": "#64748b",
}


@register(Enquiry, sites=SUPER_ONLY)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "destination", "intake", "status_badge", "status", "assigned_to", "created_at")
    list_editable = ("status", "assigned_to")
    list_filter = ("status", "destination", "intake", "course_level", "created_at")
    search_fields = ("full_name", "email", "phone", "message")
    date_hierarchy = "created_at"
    readonly_fields = ("source", "ip_address", "created_at", "updated_at")
    actions = ["export_csv", "mark_contacted"]
    fieldsets = (
        ("Student", {"fields": ("full_name", "phone", "email")}),
        ("Interest", {"fields": ("destination", "intake", "course_level", "message")}),
        ("Follow-up", {"fields": ("status", "assigned_to", "notes")}),
        ("Meta", {"fields": ("source", "ip_address", "created_at", "updated_at")}),
    )

    @admin.display(description="", ordering="status")
    def status_badge(self, obj):
        return format_html(
            '<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:{}" title="{}"></span>',
            STATUS_COLORS.get(obj.status, "#999"),
            obj.get_status_display(),
        )

    @admin.action(description="Export selected to CSV")
    def export_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="enquiries.csv"'
        writer = csv.writer(response)
        cols = ["created_at", "full_name", "phone", "email", "destination", "intake", "course_level", "status", "message", "source"]
        writer.writerow(cols)
        for e in queryset:
            writer.writerow([getattr(e, c) for c in cols])
        return response

    @admin.action(description="Mark as contacted")
    def mark_contacted(self, request, queryset):
        queryset.update(status="contacted")
