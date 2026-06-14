#!/bin/bash
# Runs on the server after each deploy (manual or GitHub Actions).
set -euo pipefail

APP_DIR="/home/lyra/lyra"

cd "$APP_DIR"

echo "==> Pulling latest code..."
git fetch origin main
git reset --hard origin/main

echo "==> Installing dependencies..."
sudo -u lyra bash -c "source venv/bin/activate && pip install -r requirements.txt"

echo "==> Django migrate & collectstatic..."
sudo -u lyra bash -c "source venv/bin/activate && python manage.py migrate --noinput"
sudo -u lyra bash -c "source venv/bin/activate && python manage.py collectstatic --noinput"

echo "==> Fixing permissions..."
chown -R lyra:www-data "$APP_DIR"
chmod -R g+rwx "$APP_DIR"

echo "==> Restarting app..."
systemctl restart lyra

echo "Deploy complete."
