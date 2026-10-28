# Deploying UniLeap to Hostinger (via GitHub)

> **Important:** Hostinger **Shared / Business / Cloud web hosting cannot run this site.** Django (Python) and PostgreSQL are supported **only on a Hostinger VPS**. Buy a **VPS (KVM 1 or KVM 2 is enough)**. You can keep your existing plan for the domain and email.

Once set up, every `git push` to `main` runs the tests on GitHub and, if they pass, updates the live site automatically.

```
your PC ──git push──▶ GitHub ──(tests pass)──SSH──▶ Hostinger VPS ──▶ https://unileapoverseas.com
                                                    Nginx → Gunicorn → Django → PostgreSQL
```

---

## 1. Push the code to GitHub (on your PC)

```bash
cd E:\Unileap
git add .
git commit -m "UniLeap website and admin panels"
git remote add origin git@github.com:<your-account>/<your-repo>.git   # your repo URL
git push -u origin main
```

`.env`, the database, `media/` and `.venv/` are in `.gitignore`. Secrets never go to GitHub.

## 2. Create the VPS (Hostinger hPanel)

1. **VPS → choose plan → Operating system: Ubuntu 24.04** (plain OS, no control panel).
2. Set a root password, then note the VPS **IP address**.

## 3. Point your domain to the VPS

In hPanel → **Domains → DNS / Nameservers** for `unileapoverseas.com`:

| Type | Name | Points to |
|---|---|---|
| A | `@` | your VPS IP |
| A | `www` | your VPS IP |

Leave your **MX** (email) records untouched so email keeps working. DNS can take from a few minutes up to a few hours.

## 4. Run the one-time setup on the VPS

Connect from your PC: `ssh root@<VPS-IP>`. Then:

```bash
nano setup_server.sh        # paste the contents of deploy/setup_server.sh, save (Ctrl+O, Enter, Ctrl+X)
bash setup_server.sh git@github.com:<your-account>/<your-repo>.git unileapoverseas.com
```

Partway through, the script **pauses and prints two keys**:

1. **Deploy key**: GitHub repo → **Settings → Deploy keys → Add deploy key** (read-only). Then press **Enter** on the VPS.
2. **Actions secrets**: GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**:
   - `VPS_HOST` = the IP the script printed
   - `VPS_SSH_KEY` = the private key the script printed (including the `BEGIN`/`END` lines)
3. **Turn on auto-deploy**: same page → **Variables** tab → **New repository variable** → `DEPLOY_ENABLED` = `true`.
   (Until this is set, pushes only run the tests and nothing is deployed.)

The script installs PostgreSQL, Nginx and Python. It creates the database with a random password, generates a secret key, loads all the website content and starts the app. It also gets a free **HTTPS certificate** (Let's Encrypt).

Finally, create your Super Admin:

```bash
sudo -u unileap bash -c 'cd ~/app && .venv/bin/python manage.py createsuperuser'
```

Open `https://unileapoverseas.com/superadmin/`. Create Website Admin users from there (**Users → action "Make selected users Website Admins"**).

## 5. Done: deploying updates from now on

```bash
git add . && git commit -m "Describe the change" && git push
```

GitHub → **Actions** tab shows progress. The **test** job runs every test against a real PostgreSQL. **deploy** then logs in to the VPS and runs `deploy/deploy.sh`, which:

- pulls the code,
- installs packages,
- runs migrations,
- collects static files,
- restarts the app.

It takes about 1–2 minutes. If a test fails, nothing is deployed.

---

## Useful commands on the VPS

| Task | Command |
|---|---|
| App status / restart | `systemctl status unileap` · `systemctl restart unileap` |
| Live app logs | `journalctl -u unileap -f` |
| Nginx errors | `tail -f /var/log/nginx/error.log` |
| Deploy manually | `sudo -u unileap bash ~unileap/app/deploy/deploy.sh` |
| Edit settings (.env) | `nano /home/unileap/app/.env` then `systemctl restart unileap` |
| Database backup | `sudo -u postgres pg_dump unileap > ~/unileap-$(date +%F).sql` |
| Renew HTTPS (automatic, to test) | `certbot renew --dry-run` |

## Email notifications for new enquiries

Add your mailbox's SMTP details to `/home/unileap/app/.env` (Hostinger email shown):

```
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.hostinger.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=info@unileapoverseas.com
EMAIL_HOST_PASSWORD=<mailbox password>
DEFAULT_FROM_EMAIL=UniLeap Overseas <info@unileapoverseas.com>
ENQUIRY_NOTIFY_EMAILS=info@unileapoverseas.com
```

Then run `systemctl restart unileap`.

## Files involved

| File | Purpose |
|---|---|
| `deploy/setup_server.sh` | One-time VPS setup |
| `deploy/deploy.sh` | Update script run on every push |
| `deploy/unileap.service` | Keeps Gunicorn (the Django app server) running |
| `deploy/nginx-unileap.conf` | Web server: HTTPS, static/media files, proxy to Django |
| `.github/workflows/deploy.yml` | GitHub Actions: test on PostgreSQL, then deploy |
