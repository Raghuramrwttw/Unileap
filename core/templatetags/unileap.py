import re

from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

HL_RE = re.compile(r"\[\[(.+?)\]\]")


@register.filter
def hl(value):
    """Render "Explore [[Top Destinations]]" with the bracketed words highlighted."""
    escaped = conditional_escape(value or "")
    return mark_safe(HL_RE.sub(r'<span class="hl">\1</span>', str(escaped)))


@register.filter
def plain(value):
    """Strip [[highlight]] markers, e.g. for <title> tags."""
    return HL_RE.sub(r"\1", value or "")


@register.filter
def attr_get(obj, name):
    return getattr(obj, name, "")


@register.filter
def split(value, sep=None):
    return value.split(sep)


@register.filter
def get_param(querydict, key):
    return querydict.get(key, "")


@register.simple_tag(takes_context=True)
def query_replace(context, **kwargs):
    """Return the current querystring with some keys replaced (used for pagination)."""
    query = context["request"].GET.copy()
    for key, value in kwargs.items():
        query[key] = value
    return query.urlencode()
