#!/usr/bin/env bash
# Pull the latest code and restart the app. Run by GitHub Actions on every push to main
# (or manually on the VPS as the unileap user: bash ~/app/deploy/deploy.sh).
set -euo pipefail

cd "$(dirname "$0")/.."

git fetch --quiet origin main
git reset --hard origin/main

.venv/bin/pip install -r requirements.txt -q
.venv/bin/python manage.py migrate --noinput
.venv/bin/python manage.py collectstatic --noinput -v 0
.venv/bin/python manage.py check --deploy --fail-level ERROR

sudo systemctl restart unileap
echo "Deployed $(git rev-parse --short HEAD) at $(date)"
