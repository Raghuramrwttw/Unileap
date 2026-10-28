import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from .forms import EnquiryForm

logger = logging.getLogger(__name__)


def _wants_json(request):
    return request.headers.get("x-requested-with") == "XMLHttpRequest" or "application/json" in request.headers.get(
        "accept", ""
    )


def _notify(enquiry):
    if not settings.ENQUIRY_NOTIFY_EMAILS:
        return
    body = "\n".join(
        [
            f"Name: {enquiry.full_name}",
            f"Phone: {enquiry.phone}",
            f"Email: {enquiry.email}",
            f"Destination: {enquiry.destination}",
            f"Intake: {enquiry.intake}",
            f"Course level: {enquiry.course_level or '-'}",
            f"Message: {enquiry.message or '-'}",
            f"Submitted from: {enquiry.source}",
        ]
    )
    try:
        send_mail(f"New enquiry: {enquiry.full_name}", body, None, settings.ENQUIRY_NOTIFY_EMAILS)
    except Exception:  # never lose a lead because email is misconfigured
        logger.exception("Could not send enquiry notification email")


@require_POST
def submit_enquiry(request):
    form = EnquiryForm(request.POST)
    back = request.POST.get("next") or request.META.get("HTTP_REFERER") or "/"
    if not url_has_allowed_host_and_scheme(back, allowed_hosts={request.get_host()}):
        back = "/"

    if form.is_valid():
        if not form.is_spam():
            enquiry = form.save(commit=False)
            enquiry.ip_address = request.META.get("REMOTE_ADDR")
            enquiry.save()
            _notify(enquiry)
        # The thank-you page only shows after a real submission (see core.views.thank_you).
        request.session["enquiry_submitted"] = form.cleaned_data["full_name"].split()[0]
        thank_you = reverse("core:thank_you")
        if _wants_json(request):
            return JsonResponse({"ok": True, "redirect": thank_you})
        return redirect(thank_you)

    if _wants_json(request):
        return JsonResponse({"ok": False, "errors": form.errors}, status=400)
    for field, errors in form.errors.items():
        messages.error(request, f"{form.fields[field].label if field in form.fields else field}: {errors[0]}")
    return redirect(back)
