"""Restore the original Home banner (with the counselling form) that 0003 replaced.

Only applies when the banner still has the text 0003 put there, so admin edits are kept.
"""

from django.db import migrations

from core import seed_data

V2_TITLE = "A Brighter Global Future [[Starts Here]]"
V2_FEATURES = ["Personalised Guidance", "University Shortlisting", "End-to-End Support", "Visa Guidance"]


def forwards(apps, schema_editor):
    PageHero = apps.get_model("core", "PageHero")
    HeroFeature = apps.get_model("core", "HeroFeature")

    hero = PageHero.objects.filter(page="home", title=V2_TITLE).first()
    if not hero:
        return
    original = seed_data.HEROES["home"]
    for field in ("eyebrow", "title", "subtitle", "show_counselling_form"):
        setattr(hero, field, original[field])
    hero.save()

    labels = list(HeroFeature.objects.filter(hero=hero).order_by("order", "id").values_list("label", flat=True))
    if labels == V2_FEATURES:
        HeroFeature.objects.filter(hero=hero).delete()
        for i, (icon, label) in enumerate(seed_data.HOME_HERO_FEATURES):
            HeroFeature.objects.create(hero=hero, icon=icon, label=label, order=i)


class Migration(migrations.Migration):
    dependencies = [("core", "0003_home_v2_content")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
