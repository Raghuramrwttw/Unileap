import os

from django.conf import settings
from django.contrib.auth.models import Group, Permission, User
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone
from django.utils.text import slugify

from blog.models import BlogCategory, Post
from catalog.models import Course, CourseCategory, Destination, DestinationHighlight, University
from core import seed_data as data
from core.models import (
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
from loans.models import Lender, LoanType

# Website Admins get full rights on every model in these apps, except the ones listed.
CONTENT_APPS = ["core", "catalog", "loans", "blog"]
EXCLUDED_MODELS = {"subscriber"}


class Command(BaseCommand):
    help = "Create the Website Admin role and load the initial website content (safe to run multiple times)."

    def add_arguments(self, parser):
        parser.add_argument("--no-content", action="store_true", help="Only set up roles/permissions.")
        parser.add_argument(
            "--demo-users",
            action="store_true",
            help="Create demo accounts 'superadmin' and 'webadmin' (password from DEMO_PASSWORD env, default Unileap@2026).",
        )

    @transaction.atomic
    def handle(self, *args, **opts):
        group = self.setup_roles()
        if not opts["no_content"]:
            self.load_content()
        if opts["demo_users"]:
            self.create_demo_users(group)
        self.stdout.write(self.style.SUCCESS("UniLeap setup complete."))

    # ---- roles -----------------------------------------------------------------------

    def setup_roles(self):
        group, _ = Group.objects.get_or_create(name=settings.WEBSITE_ADMIN_GROUP)
        perms = Permission.objects.filter(content_type__app_label__in=CONTENT_APPS).exclude(
            content_type__model__in=EXCLUDED_MODELS
        )
        group.permissions.set(perms)
        self.stdout.write(f"Role '{group.name}' has {perms.count()} permissions.")
        return group

    def create_demo_users(self, group):
        password = os.getenv("DEMO_PASSWORD", "Unileap@2026")
        su, created = User.objects.get_or_create(
            username="superadmin", defaults={"email": "superadmin@unileapoverseas.com", "first_name": "Super"}
        )
        su.is_staff = su.is_superuser = True
        if created:
            su.set_password(password)
        su.save()
        wa, created_wa = User.objects.get_or_create(
            username="webadmin", defaults={"email": "webadmin@unileapoverseas.com", "first_name": "Website"}
        )
        wa.is_staff, wa.is_superuser = True, False
        if created_wa:
            wa.set_password(password)
        wa.save()
        wa.groups.add(group)
        self.stdout.write(
            self.style.WARNING(
                f"Demo users ready: superadmin / webadmin (password '{password}' if newly created). Change these passwords!"
            )
        )

    # ---- content ---------------------------------------------------------------------

    def load_content(self):
        site = SiteSettings.load()
        for field, value in data.SITE.items():
            if not getattr(site, field):
                setattr(site, field, value)
        site.save()

        for page, cfg in data.HEROES.items():
            cfg = dict(cfg)
            features = cfg.pop("features", [])
            hero, created = PageHero.objects.get_or_create(page=page, defaults=cfg)
            if created:
                for i, (icon, label) in enumerate(features):
                    HeroFeature.objects.create(hero=hero, icon=icon, label=label, order=i)

        for key, cfg in data.SECTIONS.items():
            Section.objects.get_or_create(key=key, defaults=cfg)

        self._seed_list(FeatureItem, "group", data.FEATURES, lambda row: dict(zip(("icon", "title", "description", "note"), row)))
        if not Service.objects.exists():
            for i, (title, icon, desc, link) in enumerate(data.SERVICES):
                Service.objects.create(title=title, icon=icon, description=desc, link=link, order=i)
        self._seed_list(ProcessStep, "group", data.STEPS, lambda row: dict(zip(("icon", "title", "description"), row)))
        self._seed_list(FAQ, "group", data.FAQS, lambda row: {"question": row[0], "answer": f"<p>{row[1]}</p>"})
        if not Stat.objects.exists():
            for i, (icon, value, label) in enumerate(data.STATS):
                Stat.objects.create(icon=icon, value=value, label=label, order=i)

        categories = {}
        for i, (name, slug, icon) in enumerate(data.COURSE_CATEGORIES):
            categories[slug], _ = CourseCategory.objects.get_or_create(slug=slug, defaults={"name": name, "icon": icon, "order": i})

        destinations = {}
        for i, cfg in enumerate(data.DESTINATIONS):
            cfg = dict(cfg)
            highlights = cfg.pop("highlights")
            dest, created = Destination.objects.get_or_create(slug=cfg["slug"], defaults={**cfg, "order": i})
            destinations[dest.slug] = dest
            if created:
                for j, (icon, text) in enumerate(highlights):
                    DestinationHighlight.objects.create(destination=dest, icon=icon, text=text, order=j)

        for i, (name, dest_slug, city, kind, est, photo, top, courses) in enumerate(data.UNIVERSITIES):
            uni, created = University.objects.get_or_create(
                slug=_slug(name),
                defaults={
                    "name": name,
                    "destination": destinations[dest_slug],
                    "city": city,
                    "institution_type": kind,
                    "established": est,
                    "image_url": data.img(photo, 800),
                    "is_top": top,
                    "order": i,
                    "description": f"<p>{name} is a well-regarded {dict(University.TYPES)[kind].lower()} in {city}. "
                    "Speak to our counsellors for the latest entry requirements, scholarships and application deadlines.</p>",
                },
            )
            if created:
                for j, (cname, cat, level, duration, intakes, fee, popular) in enumerate(courses):
                    Course.objects.create(
                        university=uni, name=cname, category=categories[cat], level=level, duration=duration,
                        intakes=intakes, tuition_fee=fee, is_popular=popular, order=j,
                    )

        if not Lender.objects.exists():
            for i, (name, color) in enumerate(data.LENDERS):
                Lender.objects.create(name=name, brand_color=color, order=i)
        if not LoanType.objects.exists():
            for i, (title, icon, subtitle, points, style) in enumerate(data.LOAN_TYPES):
                LoanType.objects.create(title=title, icon=icon, subtitle=subtitle, points=points, style=style, order=i)

        blog_categories = {}
        for i, (name, slug, icon) in enumerate(data.BLOG_CATEGORIES):
            blog_categories[slug], _ = BlogCategory.objects.get_or_create(slug=slug, defaults={"name": name, "icon": icon, "order": i})
        for title, slug, cat, tag, color, photo, date, featured, excerpt, content in data.POSTS:
            Post.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title, "category": blog_categories[cat], "tag": tag, "tag_color": color,
                    "image_url": data.img(photo, 900), "excerpt": excerpt, "content": content,
                    "status": Post.PUBLISHED, "is_featured": featured,
                    "published_at": timezone.make_aware(date),
                },
            )

        if not TeamMember.objects.exists():
            for i, (name, role, bio) in enumerate(data.TEAM):
                TeamMember.objects.create(name=name, role=role, bio=bio, order=i)
        if not Testimonial.objects.exists():
            for i, (name, detail, quote) in enumerate(data.TESTIMONIALS):
                Testimonial.objects.create(name=name, detail=detail, quote=quote, order=i)
        if not Partner.objects.exists():
            for i, (name, desc) in enumerate(data.PARTNERS):
                Partner.objects.create(name=name, description=desc, order=i)
        for title, slug, content in data.LEGAL_PAGES:
            LegalPage.objects.get_or_create(slug=slug, defaults={"title": title, "content": content})

        self.stdout.write("Website content loaded.")

    def _seed_list(self, model, group_field, groups, to_fields):
        """Create items for each group that has no items yet (so edits are never overwritten)."""
        for group, rows in groups.items():
            if model.objects.filter(**{group_field: group}).exists():
                continue
            for i, row in enumerate(rows):
                model.objects.create(**{group_field: group, "order": i, **to_fields(row)})


def _slug(name):
    return slugify(name.replace("(", "").replace(")", ""))
