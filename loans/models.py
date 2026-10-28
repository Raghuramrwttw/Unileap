from django.db import models

from core.models import ICON_HELP, Orderable, WithImage


class Lender(Orderable, WithImage):
    name = models.CharField(max_length=100)
    brand_color = models.CharField(max_length=20, default="#0a2350", help_text="Text colour when no logo is uploaded.")
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class LoanType(Orderable):
    STYLES = [("blue", "Blue"), ("amber", "Amber")]

    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=60, help_text=ICON_HELP)
    subtitle = models.CharField(max_length=200)
    points = models.TextField(help_text="One bullet point per line.")
    style = models.CharField(max_length=10, choices=STYLES, default="blue")

    def __str__(self):
        return self.title

    @property
    def point_list(self):
        return [p.strip() for p in self.points.splitlines() if p.strip()]
