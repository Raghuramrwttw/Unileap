from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post
from catalog.models import Destination, University
from core.models import LegalPage


class StaticSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return [
            "core:home",
            "core:counselling",
            "catalog:destinations",
            "catalog:compare",
            "catalog:universities",
            "catalog:courses",
            "catalog:top_universities",
            "catalog:popular_courses",
            "loans:loan",
            "blog:list",
            "core:about",
            "core:team",
            "core:partners",
            "core:testimonials",
            "core:contact",
            "core:faq",
        ]

    def location(self, item):
        return reverse(item)


class ActiveSitemap(Sitemap):
    model = None

    def items(self):
        return self.model.objects.filter(is_active=True)


class DestinationSitemap(ActiveSitemap):
    model = Destination


class UniversitySitemap(ActiveSitemap):
    model = University


class LegalSitemap(ActiveSitemap):
    model = LegalPage
    priority = 0.3


class PostSitemap(Sitemap):
    def items(self):
        return Post.objects.published()

    def lastmod(self, obj):
        return obj.updated_at


SITEMAPS = {
    "static": StaticSitemap,
    "destinations": DestinationSitemap,
    "universities": UniversitySitemap,
    "blog": PostSitemap,
    "pages": LegalSitemap,
}
