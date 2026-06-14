# LYRA Platform

Phase 1 informative website — Django + automated deploy to DigitalOcean.

## Live stack
- **Django 5** + Gunicorn
- **Nginx** reverse proxy
- **GitHub Actions** auto-deploy on push to `main`

---

## First-time deployment (step by step)

### Part A — Push code to GitHub (on your PC)

Already done if you followed the setup. Repo: https://github.com/ahmadhjy/Lyra

### Part B — Create DigitalOcean Droplet

1. Go to [DigitalOcean](https://cloud.digitalocean.com) → **Create** → **Droplets**
2. Choose:
   - **Region:** Frankfurt (`FRA1`) — best for Qatar
   - **OS:** Ubuntu 24.04 LTS
   - **Size:** ~$32/mo (2 vCPU, 4 GB RAM)
   - **Authentication:** SSH key (add your PC's public key)
3. Create Droplet and copy the **IP address**

### Part C — One-time server setup

**1. SSH into the server** (from PowerShell on your PC):

```powershell
ssh root@YOUR_DROPLET_IP
```

**2. Run the setup script:**

```bash
git clone https://github.com/ahmadhjy/Lyra.git /home/lyra/lyra
bash /home/lyra/lyra/deploy/setup_server.sh
```

When prompted, enter your **Droplet IP** for Nginx.

**3. Configure environment:**

```bash
nano /home/lyra/lyra/.env
```

Set:

```env
DJANGO_DEBUG=False
DJANGO_SECRET_KEY=your-long-random-secret
DJANGO_ALLOWED_HOSTS=YOUR_DROPLET_IP
DJANGO_CSRF_TRUSTED_ORIGINS=
```

Generate a secret key:

```bash
/home/lyra/lyra/venv/bin/python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**4. Restart the app:**

```bash
systemctl restart lyra
```

**5. Open in browser:** `http://YOUR_DROPLET_IP`

---

### Part D — Auto-deploy (GitHub Actions)

After every `git push` to `main`, the site updates automatically.

**1. Create a deploy SSH key** (on your PC, PowerShell):

```powershell
ssh-keygen -t ed25519 -C "github-actions-lyra" -f $env:USERPROFILE\.ssh\lyra_deploy_key -N '""'
```

**2. Add the public key to the Droplet** (SSH as root):

```bash
mkdir -p /root/.ssh
nano /root/.ssh/authorized_keys
```

Paste the contents of `lyra_deploy_key.pub` (from your PC):

```powershell
Get-Content $env:USERPROFILE\.ssh\lyra_deploy_key.pub
```

**3. Add GitHub Secrets**

Go to: **GitHub repo → Settings → Secrets and variables → Actions → New repository secret**

| Secret name | Value |
|-------------|-------|
| `DROPLET_HOST` | Your Droplet IP |
| `DROPLET_USER` | `root` |
| `DROPLET_SSH_KEY` | Full contents of `lyra_deploy_key` (private key) |

**4. Test:** push any change to `main` → check **Actions** tab on GitHub.

---

## Daily workflow (after setup)

```powershell
cd C:\Users\ME\Desktop\Lyra
git add .
git commit -m "Describe your change"
git push
```

GitHub Actions deploys in ~30 seconds. No manual server steps needed.

---

## Manual deploy (if needed)

SSH to server:

```bash
bash /home/lyra/lyra/deploy/update.sh
```

---

## Useful server commands

```bash
systemctl status lyra       # Is the app running?
systemctl restart lyra      # Restart app
journalctl -u lyra -f       # Live logs
nginx -t                    # Test Nginx config
```

---

## Adding a domain + SSL (later)

1. Point domain A record → Droplet IP (Cloudflare)
2. Update `.env` with domain in `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS`
3. On server:

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d yourdomain.com -d www.yourdomain.com
systemctl restart lyra
```
