from io import StringIO

from django.conf import settings
from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from blog.models import Post, Subscriber
from catalog.models import Destination, University
from leads.models import Enquiry

from .models import PageHero, SiteSettings


class SeededTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("setup_unileap", stdout=StringIO())
        cls.superadmin = User.objects.create_superuser("boss", "boss@example.com", "pass12345!")
        cls.webadmin = User.objects.create_user("editor", "editor@example.com", "pass12345!", is_staff=True)
        cls.webadmin.groups.add(Group.objects.get(name=settings.WEBSITE_ADMIN_GROUP))
        cls.visitor = User.objects.create_user("visitor", "v@example.com", "pass12345!")


class PublicPagesTests(SeededTestCase):
    def test_sitemap_pages_render(self):
        uni = University.objects.first()
        post = Post.objects.published().first()
        urls = [
            "/", "/free-counselling/", "/university-shortlisting/",
            "/study-destinations/", "/study-destinations/uk/", "/compare-destinations/",
            "/universities-courses/", f"/universities-courses/{uni.slug}/", "/courses/", "/courses/?category=business",
            "/top-universities/", "/popular-courses/", "/courses/?destination=uk&intake=January&level=pg&q=marketing",
            "/education-loan/", "/blog/", "/blog/category/country-guides/", f"/blog/{post.slug}/", "/blog/?q=canada",
            "/about-us/", "/about-us/team/", "/about-us/partners/", "/about-us/testimonials/",
            "/contact/", "/faq/", "/sitemap/", "/sitemap.xml",
            "/privacy-policy/", "/terms-conditions/", "/disclaimer/",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)

    def test_loan_section_urls_redirect_to_anchor(self):
        res = self.client.get("/education-loan/eligibility/")
        self.assertRedirects(res, "/education-loan/#eligibility", fetch_redirect_response=False)

    def test_unknown_page_is_404(self):
        self.assertEqual(self.client.get("/does-not-exist/").status_code, 404)

    def test_university_filters(self):
        res = self.client.get("/universities-courses/", {"destination": "germany", "category": "engineering"})
        names = [u.name for u in res.context["page_obj"]]
        self.assertIn("RWTH Aachen University", names)
        self.assertTrue(all(u.destination.slug == "germany" for u in res.context["page_obj"]))
        res = self.client.get("/universities-courses/", {"intake": "February"})
        self.assertTrue(all(u.destination.slug == "australia" for u in res.context["page_obj"]))


class EnquiryTests(SeededTestCase):
    payload = {
        "full_name": "Test Student",
        "phone": "+91 98765 43210",
        "email": "student@example.com",
        "destination": "United Kingdom",
        "intake": "September 2027",
        "source": "/",
    }

    def test_ajax_enquiry_is_saved(self):
        res = self.client.post(reverse("enquiry"), self.payload, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertEqual(res.status_code, 200)
        self.assertTrue(res.json()["ok"])
        self.assertEqual(Enquiry.objects.get().full_name, "Test Student")
        self.assertEqual(res.json()["redirect"], "/thank-you/")
        page = self.client.get("/thank-you/")
        self.assertContains(page, "Hi Test,")
        self.assertContains(page, "What Happens")

    def test_regular_post_redirects_to_thank_you(self):
        res = self.client.post(reverse("enquiry"), self.payload)
        self.assertRedirects(res, "/thank-you/")

    def test_thank_you_needs_a_submission(self):
        self.assertRedirects(self.client.get("/thank-you/"), "/")

    def test_invalid_enquiry_returns_errors(self):
        res = self.client.post(reverse("enquiry"), {**self.payload, "phone": "12"}, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertEqual(res.status_code, 400)
        self.assertIn("phone", res.json()["errors"])
        self.assertFalse(Enquiry.objects.exists())

    def test_honeypot_blocks_spam(self):
        self.client.post(reverse("enquiry"), {**self.payload, "website": "spam"}, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertFalse(Enquiry.objects.exists())

    def test_newsletter_subscribe(self):
        self.client.post(reverse("blog:subscribe"), {"email": "a@b.com"}, HTTP_X_REQUESTED_WITH="XMLHttpRequest")
        self.assertTrue(Subscriber.objects.filter(email="a@b.com").exists())


class AdminRoleTests(SeededTestCase):
    def test_superadmin_can_use_both_panels(self):
        self.client.force_login(self.superadmin)
        self.assertEqual(self.client.get("/superadmin/").status_code, 200)
        self.assertEqual(self.client.get("/superadmin/leads/enquiry/").status_code, 200)
        self.assertEqual(self.client.get("/superadmin/auth/user/").status_code, 200)
        self.assertEqual(self.client.get("/cms/").status_code, 200)

    def test_website_admin_limited_to_cms(self):
        self.client.force_login(self.webadmin)
        self.assertEqual(self.client.get("/cms/").status_code, 200)
        for url in ["/cms/blog/post/add/", "/cms/core/pagehero/", "/cms/catalog/university/", "/cms/core/sitesettings/1/change/"]:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)
        # No access to the super admin panel, leads, users or subscribers
        self.assertEqual(self.client.get("/superadmin/").status_code, 302)
        self.assertEqual(self.client.get("/cms/leads/enquiry/").status_code, 404)
        self.assertEqual(self.client.get("/cms/auth/user/").status_code, 404)
        self.assertEqual(self.client.get("/cms/blog/subscriber/").status_code, 404)

    def test_regular_user_has_no_admin_access(self):
        self.client.force_login(self.visitor)
        self.assertEqual(self.client.get("/cms/").status_code, 302)
        self.assertEqual(self.client.get("/superadmin/").status_code, 302)

    def test_live_feed_reports_new_enquiries(self):
        self.client.force_login(self.superadmin)
        first = self.client.get("/superadmin/live/").json()
        Enquiry.objects.create(full_name="Live Lead", phone="9999999999", email="l@x.com", destination="Canada", intake="Jan 2027")
        data = self.client.get("/superadmin/live/", {"since": first["last_id"]}).json()
        self.assertEqual([i["name"] for i in data["items"]], ["Live Lead"])
        self.assertEqual(data["counts"]["new"], 1)


class ContentEditingTests(SeededTestCase):
    def test_cms_edits_show_on_website_immediately(self):
        self.client.force_login(self.webadmin)
        hero = PageHero.objects.get(page="home")
        url = f"/cms/core/pagehero/{hero.pk}/change/"
        form = self.client.get(url).context["adminform"].form
        data = {k: v for k, v in form.initial.items() if v is not None and k not in ("image",)}
        data.update({
            "page": "home",
            "title": "Fly Higher with [[UniLeap]]",
            "show_counselling_form": "on",
            "features-TOTAL_FORMS": "0",
            "features-INITIAL_FORMS": "0",
        })
        res = self.client.post(url, data)
        self.assertEqual(res.status_code, 302, getattr(res, "context", None) and res.context["adminform"].form.errors)
        self.client.logout()
        page = self.client.get("/")
        self.assertContains(page, 'Fly Higher with <span class="hl">UniLeap</span>', html=False)

    def test_site_settings_update_footer(self):
        settings_obj = SiteSettings.load()
        settings_obj.phone = "+91 90000 00000"
        settings_obj.save()
        self.assertContains(self.client.get("/contact/"), "+91 90000 00000")

    def test_hidden_destination_disappears(self):
        Destination.objects.filter(slug="germany").update(is_active=False)
        self.assertEqual(self.client.get("/study-destinations/germany/").status_code, 404)
        self.assertNotContains(self.client.get("/study-destinations/"), "Explore Germany")

    def test_draft_posts_are_hidden(self):
        post = Post.objects.published().first()
        post.status = Post.DRAFT
        post.save()
        self.assertEqual(self.client.get(post.get_absolute_url()).status_code, 404)


class HomePageTests(SeededTestCase):
    def test_home_sections(self):
        res = self.client.get("/")
        for text in ["Search Universities &amp; Courses", "Search by Course", "Top Universities", "Trending:", "More Than Admissions", "Students Guided", "Learn More", "Trusted by 500+ students", "Latest from"]:
            with self.subTest(text=text):
                self.assertContains(res, text)
        self.assertEqual(len(res.context["posts"]), 3)

    def test_original_landing_parts_kept(self):
        res = self.client.get("/")
        self.assertContains(res, "Your Global Education Journey")
        self.assertContains(res, 'name="full_name"')  # counselling form in the banner
        self.assertContains(res, "Ready to Start Your Global Education Journey?")
        self.assertContains(res, 'class="site-footer"')

    def test_course_search_filters(self):
        res = self.client.get("/courses/", {"destination": "australia", "intake": "July"})
        courses = list(res.context["page_obj"])
        self.assertTrue(courses)
        self.assertTrue(all(c.university.destination.slug == "australia" and "July" in c.intakes for c in courses))
