"""Upgrade existing sites to the second home page design.

Only touches content that still has its original seeded value, so anything
an admin has already edited is left alone. Fresh installs get the same content
from `setup_unileap`.
"""

from django.db import migrations

from core import seed_data

OLD_HOME_TITLE = "Your Global Education Journey [[Starts Here]]"
OLD_WHY_TITLE = "Why Choose [[UniLeap Overseas?]]"


def forwards(apps, schema_editor):
    PageHero = apps.get_model("core", "PageHero")
    Section = apps.get_model("core", "Section")
    FeatureItem = apps.get_model("core", "FeatureItem")
    Service = apps.get_model("core", "Service")

    hero = PageHero.objects.filter(page="home", title=OLD_HOME_TITLE).first()
    if hero:
        new = seed_data.HEROES["home"]
        for field in ("eyebrow", "title", "subtitle", "script_text", "show_counselling_form"):
            setattr(hero, field, new[field])
        hero.save()

    Section.objects.filter(key="home.why", title=OLD_WHY_TITLE).update(**seed_data.HOME_WHY)
    Section.objects.filter(key="home.services", eyebrow="").update(
        **{k: v for k, v in seed_data.SECTIONS["home.services"].items() if k != "title" and k != "subtitle"}
    )
    # Only add the new sections on sites that were already seeded; setup_unileap handles fresh installs.
    if Section.objects.filter(key__startswith="home.").exists():
        Section.objects.get_or_create(key="home.cta", defaults=seed_data.HOME_CTA)
        Section.objects.get_or_create(key="home.blog", defaults=seed_data.HOME_BLOG)
        if not FeatureItem.objects.filter(group="home_trending").exists():
            for i, term in enumerate(seed_data.HOME_TRENDING):
                FeatureItem.objects.create(group="home_trending", title=term, order=i)

    for title, _icon, _desc, link in seed_data.SERVICES:
        Service.objects.filter(title=title, link="").update(link=link)


class Migration(migrations.Migration):
    dependencies = [("core", "0002_home_v2_fields")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
