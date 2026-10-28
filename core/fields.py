from django import forms
from django.db import models


class RichTextWidget(forms.Textarea):
    """WYSIWYG editor (Quill) that writes HTML back into a hidden textarea."""

    template_name = "widgets/richtext.html"

    def use_required_attribute(self, initial):
        # The textarea is hidden behind the editor; browser validation would block submit.
        return False

    class Media:
        css = {"all": ["https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.snow.css", "cms/richtext.css"]}
        js = ["https://cdn.jsdelivr.net/npm/quill@2.0.3/dist/quill.js", "cms/richtext.js"]


class RichTextField(models.TextField):
    """TextField storing HTML, edited with the rich text widget in the admin."""

    def formfield(self, **kwargs):
        kwargs["widget"] = RichTextWidget
        return super().formfield(**kwargs)
