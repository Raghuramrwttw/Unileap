from django.db import models
from django.urls import reverse

from core.fields import RichTextField
from core.models import ICON_HELP, Orderable, WithImage

# Intake months offered as search filters.
INTAKE_MONTHS = ["January", "February", "April", "May", "July", "September", "October"]


class Destination(Orderable, WithImage):
    name = models.CharField(max_length=60, help_text='Short name, e.g. "UK"')
    full_name = models.CharField(max_length=100, help_text='e.g. "United Kingdom"')
    slug = models.SlugField(unique=True, help_text='Page address, e.g. "uk" → /study-destinations/uk/')
    country_code = models.CharField(max_length=2, help_text='2-letter ISO code used for the flag, e.g. "gb", "us".')
    short_description = models.CharField(max_length=150, help_text="Shown on home page cards.")
    tagline = models.CharField(max_length=80, blank=True, help_text='Very short line, e.g. "World-class education".')
    summary = models.TextField(help_text="Shown on the Study Destinations page cards.")
    description = RichTextField(blank=True, help_text="Full content for the destination detail page.")
    currency = models.CharField(max_length=5, default="£")
    tuition_fees = models.CharField(max_length=120, blank=True, help_text="Compare table: typical tuition fees.")
    post_study_work = models.CharField(max_length=120, blank=True)
    cost_of_living = models.CharField(max_length=120, blank=True)
    pr_options = models.CharField("PR options", max_length=120, blank=True)
    popular_intakes = models.CharField(max_length=120, blank=True)
    show_on_home = models.BooleanField(default=True)

    class Meta(Orderable.Meta):
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:destination", args=[self.slug])

    @property
    def flag_url(self):
        return f"https://flagcdn.com/w80/{self.country_code.lower()}.png"


class DestinationHighlight(Orderable):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="highlights")
    icon = models.CharField(max_length=60, help_text=ICON_HELP)
    text = models.CharField(max_length=80)

    class Meta(Orderable.Meta):
        pass

    def __str__(self):
        return self.text


class CourseCategory(Orderable):
    name = models.CharField(max_length=80)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=60, help_text=ICON_HELP)
    description = models.CharField(max_length=200, blank=True)

    class Meta(Orderable.Meta):
        verbose_name_plural = "Course categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:courses") + f"?category={self.slug}"


class University(Orderable, WithImage):
    TYPES = [("public", "Public University"), ("private", "Private University"), ("college", "College")]

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=160)
    destination = models.ForeignKey(Destination, on_delete=models.PROTECT, related_name="universities")
    city = models.CharField(max_length=80)
    institution_type = models.CharField(max_length=20, choices=TYPES, default="public")
    established = models.PositiveIntegerField(null=True, blank=True)
    ranking = models.CharField(max_length=80, blank=True, help_text='e.g. "QS World Ranking #80"')
    description = RichTextField(blank=True)
    website = models.URLField(blank=True)
    is_top = models.BooleanField("Top university", default=False, help_text="Show on the Top Universities page.")

    class Meta(Orderable.Meta):
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:university", args=[self.slug])


class Course(Orderable):
    LEVELS = [
        ("ug", "Undergraduate"),
        ("pg", "Postgraduate"),
        ("diploma", "Diploma"),
        ("foundation", "Foundation"),
    ]

    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="courses")
    category = models.ForeignKey(CourseCategory, on_delete=models.PROTECT, related_name="courses")
    name = models.CharField(max_length=150)
    level = models.CharField(max_length=20, choices=LEVELS, default="pg")
    duration = models.CharField(max_length=50, blank=True, help_text='e.g. "1 year"')
    intakes = models.CharField(max_length=100, default="September", help_text='Comma separated, e.g. "January, September"')
    tuition_fee = models.PositiveIntegerField(null=True, blank=True, help_text="Per year, in the destination's currency.")
    is_popular = models.BooleanField(default=False, help_text="Show on the university card and Popular Courses page.")
    description = models.TextField(blank=True)

    class Meta(Orderable.Meta):
        ordering = ["-is_popular", "order", "name"]

    def __str__(self):
        return f"{self.name} – {self.university}"

    @property
    def intake_list(self):
        return [i.strip() for i in self.intakes.split(",") if i.strip()]
