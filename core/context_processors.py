from django.utils import timezone

from catalog.models import Destination
from leads.models import Enquiry

from .models import LegalPage, Service, SiteSettings

INTAKE_MONTHS = [(1, "January"), (5, "May"), (9, "September")]


def upcoming_intakes(count=6):
    today = timezone.localdate()
    intakes, year = [], today.year
    while len(intakes) < count:
        for month, name in INTAKE_MONTHS:
            if (year, month) > (today.year, today.month) and len(intakes) < count:
                intakes.append(f"{name} {year}")
        year += 1
    return intakes


def site(request):
    """Global template context: site settings, navigation and form choices."""
    destinations = list(Destination.objects.filter(is_active=True))
    return {
        "site": SiteSettings.load(),
        "nav_destinations": destinations,
        "footer_services": Service.objects.filter(is_active=True)[:6],
        "footer_pages": LegalPage.objects.filter(is_active=True, show_in_footer=True),
        "form_destinations": [d.full_name for d in destinations] + ["Other / Not sure"],
        "form_intakes": upcoming_intakes() + ["Not decided yet"],
        "form_levels": [value for value, _ in Enquiry.LEVELS if value],
    }
