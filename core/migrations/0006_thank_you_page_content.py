"""Add the Thank You page content to sites that were already seeded (fresh installs get it from setup_unileap)."""

from django.db import migrations

from core import seed_data


def forwards(apps, schema_editor):
    Section = apps.get_model("core", "Section")
    FeatureItem = apps.get_model("core", "FeatureItem")
    if not Section.objects.exists():
        return
    for key, defaults in seed_data.THANKS_SECTIONS.items():
        Section.objects.get_or_create(key=key, defaults=defaults)
    if not FeatureItem.objects.filter(group="thanks_next").exists():
        for i, (icon, title, description) in enumerate(seed_data.THANKS_NEXT):
            FeatureItem.objects.create(group="thanks_next", icon=icon, title=title, description=description, order=i)


class Migration(migrations.Migration):
    dependencies = [("core", "0005_thank_you_page_keys")]

    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
