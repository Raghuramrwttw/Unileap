from django.contrib import admin

from core.admin import OrderableAdmin, ThumbnailMixin
from unileap.admin_sites import register

from .models import Lender, LoanType


@register(Lender)
class LenderAdmin(ThumbnailMixin, admin.ModelAdmin):
    list_display = ("name", "thumb", "order", "is_active")
    list_editable = ("order", "is_active")


@register(LoanType)
class LoanTypeAdmin(OrderableAdmin):
    list_display = ("title", "icon_preview", "style", "order", "is_active")
