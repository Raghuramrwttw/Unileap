# UniLeap Overseas

Website and admin platform for UniLeap Overseas, built with **Django** and **PostgreSQL** from the designs in [`Prototype/`](Prototype/).

## Features

- **Public website**: every page in the sitemap prototype. That covers Home, Study Destinations (one page per country, plus a comparison table), Universities & Courses search with filters, Courses, Top Universities and Popular Courses. It also covers Education Loan, Blog (categories, search, newsletter), About (Team, Partners, Testimonials), Contact, Free Counselling, FAQs, Sitemap, the legal pages and a 404 page.
- **Lead capture**: every enquiry form submits without a page reload and is saved as an *Enquiry*. It can also be emailed to your team.
- **Two admin panels**:

| Panel | URL | Who | Can do |
|---|---|---|---|
| **Super Admin** | `/superadmin/` | Superusers | Everything: users & roles, enquiries/leads (status, assignment, CSV export), newsletter subscribers, and all website content. The dashboard shows a **live enquiry feed** that updates every few seconds and pops up a notification for each new enquiry. |
| **Website Admin** (CMS) | `/cms/` | Members of the *Website Admin* group | A WordPress-style content panel. Edit page banners, section headings, destinations, universities & courses, blog posts (rich-text editor, draft/publish/schedule), FAQs, services, stats, team, testimonials, lenders, legal pages and site settings (phone, email, address, social links). Cannot see leads or users. |

Content is read from the database on every request, so **changes made in either panel appear on the website immediately**.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt

copy .env.example .env            # then set DB_PASSWORD etc.

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Create the PostgreSQL database (once):

```bash
psql -U postgres -c "CREATE DATABASE unileap;"
```

Then:

```bash
python manage.py migrate
python manage.py setup_unileap --demo-users   # role + permissions + all prototype content + demo accounts
python manage.py runserver
```

- Website: http://127.0.0.1:8000/
- Super Admin: http://127.0.0.1:8000/superadmin/ (login: `superadmin`)
- Website Admin: http://127.0.0.1:8000/cms/ (login: `webadmin`)

The demo password is `DEMO_PASSWORD` from `.env` (default `Unileap@2026`). **Change it right away.** Leave out `--demo-users` to create your own accounts instead:

```bash
python manage.py createsuperuser        # a Super Admin
```

To add a Website Admin, the Super Admin creates a user in **Super Admin → Users**, then selects it and runs the action **"Make selected users Website Admins"**.

`setup_unileap` is safe to run again. It only adds content that is missing and never overwrites your edits.

## Editing content (Website Admin guide)

| To change… | Go to |
|---|---|
| Big banner at the top of a page (title, text, image, icons) | **Page banners** |
| A section title/subtitle (e.g. "Explore Top Study Destinations") | **Page sections** |
| Icon cards (Why choose us, loan highlights, eligibility…) | **Feature cards** (filter by group) |
| Phone, email, address, hours, social links, map, footer text | **Site settings** |
| Countries, their highlights and comparison data | **Destinations** |
| Universities and their courses | **Universities** (courses are edited inline) |
| Blog posts | **Posts**: set *Status = Published*; a future *published at* date schedules the post |

Tips:
- In titles, wrap words in `[[double brackets]]` to highlight them in blue (yellow on dark banners).
- Icons are Font Awesome class names, e.g. `fa-solid fa-graduation-cap` (browse at fontawesome.com/icons).
- Images can be uploaded, or given as an external URL.

## Tests

```bash
set DB_ENGINE=sqlite && python manage.py test core
```

The tests cover every public page, the enquiry form and spam honeypot, the permission split between the two panels, the live enquiry feed, and CMS edits showing up on the site.

## Production notes

- Set `DJANGO_DEBUG=False`, a strong `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS` and `DJANGO_CSRF_TRUSTED_ORIGINS`.
- Run `python manage.py collectstatic`. Static files are served by WhiteNoise.
- Serve `media/` (uploaded images) from your web server or object storage.
- Configure SMTP in `.env` and set `ENQUIRY_NOTIFY_EMAILS` to get an email for every new enquiry.
- The team members, testimonials, university fees and photos (from Unsplash) are **sample content** taken from the prototypes. Replace them with real data from the Website Admin panel.

## Project layout

```
unileap/   settings, URLs, the two admin sites (admin_sites.py), sitemap.xml
core/      site settings, page banners/sections, FAQs, services, team, legal pages, seed command
catalog/   destinations, universities, course categories, courses
loans/     lenders, loan types
blog/      categories, posts, newsletter subscribers
leads/     enquiries (counselling / contact form submissions)
templates/ public pages + admin dashboards     static/  CSS, JS, admin editor assets
```
