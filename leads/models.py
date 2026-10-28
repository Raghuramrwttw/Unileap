from django.conf import settings
from django.db import models


class Enquiry(models.Model):
    """A counselling / contact request submitted from any form on the website."""

    STATUSES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("in_progress", "In progress"),
        ("converted", "Converted"),
        ("closed", "Closed"),
    ]
    LEVELS = [
        ("", "Select course level"),
        ("Undergraduate", "Undergraduate"),
        ("Postgraduate", "Postgraduate"),
        ("Diploma", "Diploma"),
        ("Foundation", "Foundation"),
        ("PhD / Research", "PhD / Research"),
    ]

    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    destination = models.CharField("Preferred destination", max_length=60)
    intake = models.CharField("Preferred intake", max_length=40)
    course_level = models.CharField(max_length=40, blank=True, choices=LEVELS)
    message = models.TextField(blank=True)
    source = models.CharField(max_length=200, blank=True, help_text="Page the form was submitted from.")
    status = models.CharField(max_length=20, choices=STATUSES, default="new", db_index=True)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="enquiries"
    )
    notes = models.TextField("Internal notes", blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return f"{self.full_name} ({self.destination})"
