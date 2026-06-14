#!/bin/bash
# ONE-TIME server setup. Run as root on a fresh Ubuntu Droplet.
set -euo pipefail

APP_DIR="/home/lyra/lyra"
APP_USER="lyra"
REPO_URL="https://github.com/ahmadhjy/Lyra.git"

echo "==> Installing system packages..."
apt update
apt upgrade -y
apt install -y python3 python3-pip python3-venv nginx git ufw

echo "==> Creating app user..."
if ! id "$APP_USER" &>/dev/null; then
    adduser --disabled-password --gecos "" "$APP_USER"
fi

echo "==> Cloning repository..."
if [ ! -d "$APP_DIR/.git" ]; then
    git clone "$REPO_URL" "$APP_DIR"
fi

chown -R "$APP_USER:$APP_USER" "$APP_DIR"

echo "==> Setting up Python environment..."
cd "$APP_DIR"
sudo -u "$APP_USER" python3 -m venv venv
sudo -u "$APP_USER" bash -c "source venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt"

if [ ! -f "$APP_DIR/.env" ]; then
    cp "$APP_DIR/deploy/.env.example" "$APP_DIR/.env"
    echo ""
    echo "IMPORTANT: Edit $APP_DIR/.env (SECRET_KEY, ALLOWED_HOSTS, domain)."
    echo ""
fi

echo "==> Django setup..."
sudo -u "$APP_USER" bash -c "cd $APP_DIR && source venv/bin/activate && python manage.py migrate --noinput"
sudo -u "$APP_USER" bash -c "cd $APP_DIR && source venv/bin/activate && python manage.py collectstatic --noinput"

chown -R lyra:www-data "$APP_DIR"
chmod -R g+rwx "$APP_DIR"
chmod +x "$APP_DIR/deploy/update.sh"

echo "==> Installing Gunicorn service..."
cp "$APP_DIR/deploy/gunicorn.service" /etc/systemd/system/lyra.service
systemctl daemon-reload
systemctl enable lyra
systemctl restart lyra

echo "==> Configuring Nginx..."
read -r -p "Enter your Droplet IP or domain for Nginx server_name: " SERVER_NAME
sed "s/YOUR_DOMAIN_OR_IP/$SERVER_NAME/" "$APP_DIR/deploy/nginx-lyra.conf" > /etc/nginx/sites-available/lyra
ln -sf /etc/nginx/sites-available/lyra /etc/nginx/sites-enabled/lyra
rm -f /etc/nginx/sites-enabled/default
nginx -t
systemctl restart nginx

echo "==> Firewall..."
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable

echo ""
echo "============================================"
echo "  Server setup complete!"
echo "  Visit: http://$SERVER_NAME"
echo ""
echo "  Next steps:"
echo "  1. Edit /home/lyra/lyra/.env"
echo "  2. systemctl restart lyra"
echo "  3. Add GitHub Actions secrets for auto-deploy"
echo "============================================"
