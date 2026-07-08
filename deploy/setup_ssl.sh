#!/bin/bash
# One-time SSL setup for lyraaiqat.com (Let's Encrypt via Certbot).
# Run as root AFTER DNS A records point to this server and HTTP works.
set -euo pipefail

DOMAIN="lyraaiqat.com"
WWW="www.lyraaiqat.com"
EMAIL="${CERTBOT_EMAIL:-info@lyraaiqat.com}"
NGINX_SITE="/etc/nginx/sites-available/lyra"
APP_ENV="/home/lyra/lyra/.env"

echo "==> Installing Certbot..."
export DEBIAN_FRONTEND=noninteractive
apt update
apt install -y certbot python3-certbot-nginx

echo "==> Ensuring Nginx config is in place..."
if [ -f /home/lyra/lyra/deploy/nginx-lyra.conf ]; then
  cp /home/lyra/lyra/deploy/nginx-lyra.conf "$NGINX_SITE"
  ln -sf "$NGINX_SITE" /etc/nginx/sites-enabled/lyra
fi
nginx -t
systemctl reload nginx

echo "==> Requesting certificate for $DOMAIN and $WWW..."
certbot --nginx \
  -d "$DOMAIN" \
  -d "$WWW" \
  --non-interactive \
  --agree-tos \
  -m "$EMAIL" \
  --redirect

echo "==> Updating Django .env trusted origins for HTTPS..."
if [ -f "$APP_ENV" ]; then
  if grep -q "^DJANGO_CSRF_TRUSTED_ORIGINS=" "$APP_ENV"; then
    sed -i 's|^DJANGO_CSRF_TRUSTED_ORIGINS=.*|DJANGO_CSRF_TRUSTED_ORIGINS=https://lyraaiqat.com,https://www.lyraaiqat.com|' "$APP_ENV"
  else
    echo "DJANGO_CSRF_TRUSTED_ORIGINS=https://lyraaiqat.com,https://www.lyraaiqat.com" >> "$APP_ENV"
  fi
  if grep -q "^DJANGO_ALLOWED_HOSTS=" "$APP_ENV"; then
    sed -i 's|^DJANGO_ALLOWED_HOSTS=.*|DJANGO_ALLOWED_HOSTS=lyraaiqat.com,www.lyraaiqat.com,207.154.253.157|' "$APP_ENV"
  else
    echo "DJANGO_ALLOWED_HOSTS=lyraaiqat.com,www.lyraaiqat.com,207.154.253.157" >> "$APP_ENV"
  fi
  systemctl restart lyra
fi

echo "==> Enabling auto-renewal timer..."
systemctl enable --now certbot.timer || true
certbot renew --dry-run || true

echo ""
echo "============================================"
echo "  SSL enabled"
echo "  https://$DOMAIN"
echo "  https://$WWW"
echo "============================================"
