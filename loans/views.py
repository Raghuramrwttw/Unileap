from django.shortcuts import redirect, render

from core.models import FAQ, FeatureItem, ProcessStep, Section
from core.views import hero_for

from .models import Lender, LoanType

# /education-loan/<section>/ URLs from the sitemap jump to the matching section of the loan page.
SECTION_ANCHORS = {
    "loan-options": "loan-options",
    "eligibility": "eligibility",
    "documents": "documents",
    "lenders": "lenders",
    "process": "process",
    "faq": "faq",
}


def loan(request):
    def items(group):
        return FeatureItem.objects.filter(group=group, is_active=True)

    return render(
        request,
        "loans/loan.html",
        {
            "hero": hero_for("loan"),
            "sections": Section.for_page("loan"),
            "highlights": items("loan_highlights"),
            "eligibility": items("loan_eligibility"),
            "details": items("loan_details"),
            "documents": items("loan_documents"),
            "lenders": Lender.objects.filter(is_active=True),
            "loan_types": LoanType.objects.filter(is_active=True),
            "steps": ProcessStep.objects.filter(group="loan_process", is_active=True),
            "faqs": FAQ.objects.filter(group="loan", is_active=True),
        },
    )


def loan_section(request, section):
    anchor = SECTION_ANCHORS.get(section)
    return redirect(f"/education-loan/#{anchor}" if anchor else "/education-loan/")
