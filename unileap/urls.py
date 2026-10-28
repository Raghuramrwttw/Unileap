from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from core import views as core_views
from leads.views import submit_enquiry

from .admin_sites import super_admin_site, website_admin_site
from .sitemaps import SITEMAPS

urlpatterns = [
    path("superadmin/", super_admin_site.urls),
    path("cms/", website_admin_site.urls),
    path("enquiry/", submit_enquiry, name="enquiry"),
    path("sitemap.xml", sitemap, {"sitemaps": SITEMAPS}, name="sitemap_xml"),
    path("", include("catalog.urls")),
    path("education-loan/", include("loans.urls")),
    path("blog/", include("blog.urls")),
    path("", include("core.urls")),  # last: contains the /<slug>/ catch-all for legal pages
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = core_views.page_not_found
handler500 = core_views.server_error
