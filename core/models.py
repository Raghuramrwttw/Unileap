from django.db import models
from django.urls import reverse

from .fields import RichTextField

ICON_HELP = 'Font Awesome icon class, e.g. "fa-solid fa-graduation-cap". Browse icons at fontawesome.com/icons.'
TITLE_HELP = "Wrap words in [[double brackets]] to highlight them, e.g. \"Explore [[Top Study Destinations]]\"."


class Orderable(models.Model):
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first.")
    is_active = models.BooleanField("Visible on website", default=True)

    class Meta:
        abstract = True
        ordering = ["order", "id"]


class WithImage(models.Model):
    image = models.ImageField(upload_to="uploads/%Y/%m/", blank=True)
    image_url = models.URLField(
        "Image URL", max_length=500, blank=True, help_text="Used only when no image is uploaded."
    )

    class Meta:
        abstract = True

    @property
    def image_src(self):
        if self.image:
            return self.image.url
        return self.image_url


class SiteSettings(models.Model):
    """Global site-wide content: branding, contact details, social links, footer."""

    site_name = models.CharField(max_length=100, default="UniLeap Overseas")
    tagline = models.CharField(max_length=150, default="Your Global Education Journey Starts Here")
    logo = models.ImageField(upload_to="branding/", blank=True, help_text="Optional. Text logo is used if empty.")
    footer_about = models.TextField(
        default="We help students explore global education opportunities with the right guidance, "
        "support and resources for a brighter future."
    )
    phone = models.CharField(max_length=40, default="+91 86880 88983")
    whatsapp = models.CharField(max_length=40, blank=True, help_text="Digits only incl. country code, e.g. 919876543210")
    email = models.EmailField(default="info@unileapoverseas.com")
    email_note = models.CharField(max_length=100, default="We usually respond within 24 hours")
    city = models.CharField(max_length=100, default="Hyderabad, India")
    address = models.TextField(default="Plot No. 123, 3rd Floor, Gachibowli, Hyderabad, Telangana - 500032")
    hours = models.CharField(max_length=100, default="Mon - Sat, 9:00 AM - 6:00 PM")
    closed_note = models.CharField(max_length=100, default="Sunday: Closed")
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    map_embed_url = models.URLField(
        max_length=1000, blank=True, help_text="Google Maps → Share → Embed a map → copy the src URL."
    )
    office_image_url = models.URLField(max_length=500, blank=True)
    cta_title = models.CharField(max_length=200, default="Ready to Start Your Global Education Journey?")
    cta_subtitle = models.CharField(
        max_length=300, default="Get free expert counselling and take the first step towards your future."
    )
    cta_image_url = models.URLField(max_length=500, blank=True)
    privacy_note = models.CharField(max_length=200, default="Your details are safe with us. We respect your privacy.")
    meta_description = models.CharField(
        max_length=300,
        default="UniLeap Overseas – personalised study abroad guidance for the UK, USA, Canada, Australia, "
        "Ireland and Germany. Free counselling, university shortlisting, visa and education loan support.",
    )

    class Meta:
        verbose_name = verbose_name_plural = "Site settings"

    def __str__(self):
        return "Site settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class PageHero(WithImage):
    """The large banner at the top of each main page."""

    PAGES = [
        ("home", "Home"),
        ("about", "About Us"),
        ("destinations", "Study Destinations"),
        ("universities", "Universities & Courses"),
        ("loan", "Education Loan"),
        ("blog", "Blog"),
        ("contact", "Contact Us"),
        ("counselling", "Free Counselling"),
    ]

    page = models.CharField(max_length=30, choices=PAGES, unique=True)
    eyebrow = models.CharField(max_length=100, blank=True, help_text="Small label above the title.")
    title = models.CharField(max_length=200, help_text=TITLE_HELP)
    subtitle = models.TextField(blank=True)
    script_text = models.CharField(
        max_length=120, blank=True, help_text="Handwritten-style text on the image. Use | for line breaks."
    )
    show_counselling_form = models.BooleanField(default=False, help_text="Show the enquiry form inside the banner.")

    class Meta:
        ordering = ["page"]
        verbose_name = "Page banner"

    def __str__(self):
        return self.get_page_display()

    @property
    def script_lines(self):
        return [line.strip() for line in self.script_text.split("|") if line.strip()]


class HeroFeature(Orderable):
    hero = models.ForeignKey(PageHero, on_delete=models.CASCADE, related_name="features")
    icon = models.CharField(max_length=60, help_text=ICON_HELP)
    label = models.CharField(max_length=60)

    class Meta(Orderable.Meta):
        verbose_name = "Banner icon"

    def __str__(self):
        return self.label


class Section(WithImage):
    """Editable heading/intro text for a section of a page."""

    KEYS = [
        ("home.destinations", "Home – Study destinations"),
        ("home.courses", "Home – Course categories"),
        ("home.services", "Home – Services"),
        ("home.journey", "Home – 5 step journey"),
        ("home.why", "Home – Why choose us"),
        ("home.faq", "Home – FAQs"),
        ("home.cta", "Home – Plan your journey (call to action)"),
        ("home.blog", "Home – Latest from our blog"),
        ("about.story", "About – Who we are"),
        ("about.foundation", "About – Mission, vision & values"),
        ("about.why", "About – Why choose us"),
        ("about.cta", "About – Bottom call to action"),
        ("destinations.list", "Destinations – List"),
        ("destinations.compare", "Destinations – Compare banner"),
        ("destinations.why", "Destinations – Why study abroad"),
        ("destinations.cta", "Destinations – Bottom call to action"),
        ("universities.help", "Universities – Help banner"),
        ("loan.partners", "Loan – Lending partners"),
        ("loan.process", "Loan – Process"),
        ("loan.types", "Loan – Types of loans"),
        ("loan.eligibility", "Loan – Eligibility"),
        ("loan.details", "Loan – Loan details"),
        ("loan.documents", "Loan – Required documents"),
        ("loan.faq", "Loan – FAQs"),
        ("loan.cta", "Loan – Personalised guidance box"),
        ("blog.categories", "Blog – Categories"),
        ("blog.latest", "Blog – Latest articles"),
        ("blog.newsletter", "Blog – Newsletter box"),
        ("contact.form", "Contact – Get in touch form"),
        ("contact.info", "Contact – Contact information"),
        ("contact.follow", "Contact – Follow us"),
        ("contact.location", "Contact – Our location"),
        ("contact.online", "Contact – Can't visit us"),
        ("contact.faq", "Contact – FAQs"),
        ("contact.cta", "Contact – Still have questions"),
        ("thanks.hero", "Thank you page – Banner"),
        ("thanks.next", "Thank you page – What happens next"),
        ("thanks.explore", "Thank you page – In the meantime, explore"),
        ("team.intro", "Team page – Intro"),
        ("partners.intro", "Partners page – Intro"),
        ("testimonials.intro", "Testimonials page – Intro"),
    ]

    key = models.CharField(max_length=50, choices=KEYS, unique=True)
    eyebrow = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=200, blank=True, help_text=TITLE_HELP)
    subtitle = models.TextField(blank=True)
    body = RichTextField(blank=True)
    button_text = models.CharField(max_length=60, blank=True)
    button_link = models.CharField(max_length=200, blank=True)
    script_text = models.CharField(max_length=120, blank=True, help_text="Handwritten-style text. Use | for line breaks.")

    class Meta:
        ordering = ["key"]
        verbose_name = "Page section"

    def __str__(self):
        return self.get_key_display()

    @property
    def script_lines(self):
        return [line.strip() for line in self.script_text.split("|") if line.strip()]

    @classmethod
    def for_page(cls, page):
        """Return {"destinations": Section, ...} for every section of the given page."""
        prefix = f"{page}."
        return {s.key[len(prefix):]: s for s in cls.objects.filter(key__startswith=prefix)}


class FeatureItem(Orderable):
    """Generic icon + title + description card used across many sections."""

    GROUPS = [
        ("home_why", "Home – Why choose us"),
        ("home_trending", "Home – Trending searches (chips under the search box)"),
        ("about_why", "About – Why choose us"),
        ("about_foundation", "About – Mission & vision"),
        ("about_values", "About – Our values (bullet list)"),
        ("destinations_why", "Destinations – Why study abroad"),
        ("compare_factors", "Destinations – Compare factors"),
        ("universities_help", "Universities – Help banner points"),
        ("loan_highlights", "Loan – Highlight cards"),
        ("loan_eligibility", "Loan – Eligibility criteria"),
        ("loan_details", "Loan – Loan details"),
        ("loan_documents", "Loan – Required documents"),
        ("contact_online", "Contact – Online counselling points"),
        ("contact_cta", "Contact – Still have questions points"),
        ("thanks_next", "Thank you page – What happens next steps"),
    ]

    group = models.CharField(max_length=40, choices=GROUPS, db_index=True)
    icon = models.CharField(max_length=60, blank=True, help_text=ICON_HELP)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    note = models.CharField(max_length=100, blank=True, help_text='Optional small note, e.g. "(Varies by lender)".')

    class Meta(Orderable.Meta):
        ordering = ["group", "order", "id"]
        verbose_name = "Feature card"

    def __str__(self):
        return self.title


class Service(Orderable):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=60, help_text=ICON_HELP)
    description = models.TextField()
    link = models.CharField(
        max_length=200, blank=True, help_text='"Learn More" link, e.g. /education-loan/. Defaults to the counselling page.'
    )

    def __str__(self):
        return self.title


class ProcessStep(Orderable):
    GROUPS = [("home_journey", "Home – Study abroad journey"), ("loan_process", "Loan – Loan process")]

    group = models.CharField(max_length=30, choices=GROUPS, db_index=True)
    icon = models.CharField(max_length=60, blank=True, help_text=ICON_HELP)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    class Meta(Orderable.Meta):
        ordering = ["group", "order", "id"]
        verbose_name = "Process step"

    def __str__(self):
        return self.title


class FAQ(Orderable):
    GROUPS = [
        ("general", "General"),
        ("home", "Home page"),
        ("loan", "Education loan"),
        ("contact", "Contact page"),
    ]

    group = models.CharField(max_length=20, choices=GROUPS, default="general", db_index=True)
    question = models.CharField(max_length=255)
    answer = RichTextField()

    class Meta(Orderable.Meta):
        ordering = ["group", "order", "id"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question


class Stat(Orderable):
    icon = models.CharField(max_length=60, help_text=ICON_HELP)
    value = models.CharField(max_length=20, help_text='e.g. "500+" or "95%"')
    label = models.CharField(max_length=60)

    class Meta(Orderable.Meta):
        verbose_name = "Statistic"

    def __str__(self):
        return f"{self.value} {self.label}"


class TeamMember(Orderable, WithImage):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Partner(Orderable, WithImage):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Testimonial(Orderable, WithImage):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=150, help_text='e.g. "MSc Data Science, University of Leicester"')
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5, choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return self.name


class LegalPage(models.Model):
    """Free-form pages such as Privacy Policy, Terms & Conditions and Disclaimer."""

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, help_text='The page address, e.g. "privacy-policy" → /privacy-policy/')
    content = RichTextField()
    show_in_footer = models.BooleanField(default=True)
    is_active = models.BooleanField("Published", default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Page (legal / utility)"
        verbose_name_plural = "Pages (legal / utility)"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:page", args=[self.slug])
