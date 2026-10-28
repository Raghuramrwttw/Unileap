from django import forms

from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    # Honeypot: real users never see or fill this field.
    website = forms.CharField(required=False, widget=forms.HiddenInput)

    class Meta:
        model = Enquiry
        fields = ["full_name", "phone", "email", "destination", "intake", "course_level", "message", "source"]

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        digits = [c for c in phone if c.isdigit()]
        if len(digits) < 7:
            raise forms.ValidationError("Please enter a valid phone number.")
        return phone

    def is_spam(self):
        return bool(self.data.get("website"))
