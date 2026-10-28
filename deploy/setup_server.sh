#!/usr/bin/env bash
# One-time setup of a fresh Hostinger VPS (Ubuntu 24.04 template) for UniLeap.
#
# Usage (as root, on the VPS):
#   Copy this file to the VPS (e.g. nano setup_server.sh and paste), then:
#   bash setup_server.sh <github-repo-url> <domain>
# Example:
#   bash setup_server.sh git@github.com:you/unileap.git unileapoverseas.com
# Use the SSH form of the repo URL (git@github.com:...) so the deploy key works for private repos.
set -euo pipefail

REPO_URL="${1:?GitHub repo URL required}"
DOMAIN="${2:?domain required, e.g. unileapoverseas.com}"
APP_USER="unileap"
APP_DIR="/home/${APP_USER}/app"
DB_NAME="unileap"
DB_USER="unileap"
DB_PASS="$(openssl rand -hex 16)"
SECRET_KEY="$(openssl rand -hex 32)"

echo "==> Installing system packages"
apt-get update -y
apt-get install -y python3 python3-venv python3-dev build-essential git nginx \
  postgresql postgresql-contrib libpq-dev certbot python3-certbot-nginx ufw

echo "==> Firewall"
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable

python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 12) else 1)' || {
  echo "!! Python 3.12+ is required (Django 6). Reinstall the VPS with the Ubuntu 24.04 template."; exit 1; }

echo "==> App user"
id -u "$APP_USER" >/dev/null 2>&1 || adduser --disabled-password --gecos "" "$APP_USER"
SSH_DIR="/home/${APP_USER}/.ssh"
sudo -u "$APP_USER" mkdir -p "$SSH_DIR" && chmod 700 "$SSH_DIR"

# Key 1: lets this server pull the (private) GitHub repo.
if [ ! -f "$SSH_DIR/github_deploy" ]; then
  sudo -u "$APP_USER" ssh-keygen -t ed25519 -N "" -C "unileap-vps" -f "$SSH_DIR/github_deploy" -q
  sudo -u "$APP_USER" bash -c "printf 'Host github.com\n  IdentityFile ~/.ssh/github_deploy\n  StrictHostKeyChecking accept-new\n' > $SSH_DIR/config"
fi
# Key 2: lets GitHub Actions log in to this server to run deploy.sh.
if [ ! -f "$SSH_DIR/actions" ]; then
  sudo -u "$APP_USER" ssh-keygen -t ed25519 -N "" -C "github-actions" -f "$SSH_DIR/actions" -q
  cat "$SSH_DIR/actions.pub" >> "$SSH_DIR/authorized_keys"
  chown "$APP_USER:$APP_USER" "$SSH_DIR/authorized_keys" && chmod 600 "$SSH_DIR/authorized_keys"
fi

cat <<EOF

---------------------------------------------------------------------
 ACTION NEEDED in GitHub (repo -> Settings):

 1) Deploy keys -> Add deploy key  (title: hostinger-vps, read-only)
$(cat "$SSH_DIR/github_deploy.pub")

 2) Secrets and variables -> Actions -> New repository secret
    VPS_HOST    = $(curl -s -4 ifconfig.me || hostname -I | awk '{print $1}')
    VPS_SSH_KEY = (everything below, including the BEGIN/END lines)
$(cat "$SSH_DIR/actions")
---------------------------------------------------------------------
EOF
read -r -p "Press Enter once the deploy key is added in GitHub... "

echo "==> PostgreSQL database"
sudo -u postgres psql -tc "SELECT 1 FROM pg_roles WHERE rolname='${DB_USER}'" | grep -q 1 \
  || sudo -u postgres psql -c "CREATE USER ${DB_USER} WITH PASSWORD '${DB_PASS}';"
sudo -u postgres psql -tc "SELECT 1 FROM pg_database WHERE datname='${DB_NAME}'" | grep -q 1 \
  || sudo -u postgres psql -c "CREATE DATABASE ${DB_NAME} OWNER ${DB_USER};"

echo "==> Code"
if [ ! -d "$APP_DIR/.git" ]; then
  sudo -u "$APP_USER" git clone "$REPO_URL" "$APP_DIR"
fi

echo "==> Environment file"
if [ ! -f "$APP_DIR/.env" ]; then
  cat > "$APP_DIR/.env" <<EOF
DJANGO_SECRET_KEY=${SECRET_KEY}
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=${DOMAIN},www.${DOMAIN}
DJANGO_CSRF_TRUSTED_ORIGINS=https://${DOMAIN},https://www.${DOMAIN}
# Turned on after the HTTPS certificate is installed (below).
DJANGO_SECURE_SSL_REDIRECT=False
DB_NAME=${DB_NAME}
DB_USER=${DB_USER}
DB_PASSWORD=${DB_PASS}
DB_HOST=localhost
DB_PORT=5432
ENQUIRY_NOTIFY_EMAILS=info@unileapoverseas.com
EOF
  chown "$APP_USER:$APP_USER" "$APP_DIR/.env"
  chmod 600 "$APP_DIR/.env"
fi

echo "==> Python environment, database tables and content"
sudo -u "$APP_USER" bash -c "
  cd $APP_DIR
  python3 -m venv .venv
  .venv/bin/pip install --upgrade pip -q
  .venv/bin/pip install -r requirements.txt -q
  .venv/bin/python manage.py migrate --noinput
  .venv/bin/python manage.py setup_unileap
  .venv/bin/python manage.py collectstatic --noinput
  mkdir -p media
"

echo "==> Gunicorn service"
cp "$APP_DIR/deploy/unileap.service" /etc/systemd/system/unileap.service
systemctl daemon-reload
systemctl enable --now unileap

echo "==> Nginx"
sed "s/__DOMAIN__/${DOMAIN}/g" "$APP_DIR/deploy/nginx-unileap.conf" > /etc/nginx/sites-available/unileap
ln -sf /etc/nginx/sites-available/unileap /etc/nginx/sites-enabled/unileap
rm -f /etc/nginx/sites-enabled/default
chmod 711 "/home/${APP_USER}"
nginx -t && systemctl reload nginx

echo "==> Allow the deploy user to restart the app without a password"
echo "${APP_USER} ALL=NOPASSWD: /bin/systemctl restart unileap, /usr/bin/systemctl restart unileap" > /etc/sudoers.d/unileap
chmod 440 /etc/sudoers.d/unileap

echo "==> HTTPS certificate (needs the domain's DNS already pointing at this server)"
if certbot --nginx -d "$DOMAIN" -d "www.$DOMAIN" --non-interactive --agree-tos -m "info@${DOMAIN}" --redirect; then
  sed -i 's/^DJANGO_SECURE_SSL_REDIRECT=False/DJANGO_SECURE_SSL_REDIRECT=True/' "$APP_DIR/.env"
  systemctl restart unileap
else
  echo "!! Certificate not issued yet. Point DNS to this server, then run:"
  echo "   certbot --nginx -d $DOMAIN -d www.$DOMAIN --redirect"
fi

cat <<EOF

=====================================================================
 UniLeap is installed.
 Site:          http://${DOMAIN}  (https once the certificate is issued)
 Create your Super Admin:
   sudo -u ${APP_USER} bash -c 'cd ${APP_DIR} && .venv/bin/python manage.py createsuperuser'
 Database password is stored in ${APP_DIR}/.env
=====================================================================
EOF
