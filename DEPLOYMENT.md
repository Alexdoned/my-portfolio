# PythonAnywhere Deployment Guide for My Portfolio

This guide describes how to take your Django 5 portfolio from local development to production on PythonAnywhere.

## 1. Local Project Preparation

### 1.1 Create and activate a virtual environment

```powershell
cd C:\Users\Degreat\Desktop\All-Projects\My-portfolio
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 1.2 Install project dependencies

```powershell
pip install django python-dotenv pillow
```

### 1.3 Generate `requirements.txt`

```powershell
pip freeze > requirements.txt
```

### 1.4 Confirm `.gitignore`

Make sure your `.gitignore` includes:

```gitignore
__pycache__/
*.py[cod]
*.log
.env
.env.*
.venv/
venv/
*.sqlite3
db.sqlite3
media/
staticfiles/
.DS_Store
.vscode/
```

### 1.5 Git initialization

```powershell
git init
git add .
git commit -m "Initial portfolio project"
```

### 1.6 GitHub repository setup

Create a GitHub repo and push your code:

```powershell
git remote add origin https://github.com/Alexdoned/<repo-name>.git
git branch -M main
git push -u origin main
```

> Replace `<repo-name>` with the repository name you want on GitHub.

## 2. PythonAnywhere Setup

### 2.1 Account creation

1. Open https://www.pythonanywhere.com.
2. Sign up for a free or paid account.
3. Confirm your email and log in.

### 2.2 Dashboard overview

Important tabs:
- **Dashboard**: account summary and quick links.
- **Consoles**: start Bash, Python, and database consoles.
- **Files**: upload, browse, and edit files.
- **Web**: configure your hosted application.
- **Databases**: manage database files.

### 2.3 Bash console usage

From PythonAnywhere:
- Go to **Consoles**
- Start a **Bash** console

### 2.4 Create a virtual environment on PythonAnywhere

In Bash:

```bash
cd ~
python3.12 -m venv myportfolio-venv
source myportfolio-venv/bin/activate
pip install --upgrade pip
```

### 2.5 Upload your project from GitHub

Clone your repository:

```bash
cd ~
git clone https://github.com/Alexdoned/<repo-name>.git
cd <repo-name>
```

## 3. Django Configuration

### 3.1 Configure `settings.py` for production

Your project already uses environment variables in `myportfolio/settings.py`. Confirm these key production settings:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "replace-this-secret")
DEBUG = os.getenv("DJANGO_DEBUG", "False").lower() in ("1", "true", "yes")
ALLOWED_HOSTS = [host.strip() for host in os.getenv("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",") if host.strip()]
CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", "http://localhost,https://127.0.0.1").split(",") if origin.strip()]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### 3.2 Configure environment variables

On PythonAnywhere, set these in the Web tab under **Environment variables**:

- `DJANGO_SECRET_KEY` = a secure random string
- `DJANGO_DEBUG` = `False`
- `DJANGO_ALLOWED_HOSTS` = `yourusername.pythonanywhere.com`
- `DJANGO_CSRF_TRUSTED_ORIGINS` = `https://yourusername.pythonanywhere.com`

For example:

```text
DJANGO_SECRET_KEY=your-long-secure-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourusername.pythonanywhere.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://yourusername.pythonanywhere.com
```

### 3.3 Configure WSGI

In the PythonAnywhere **Web** tab, open the WSGI configuration file and ensure it contains:

```python
import os
import sys

path = '/home/yourusername/<repo-name>'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myportfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Replace `yourusername` and `<repo-name>` with your PythonAnywhere username and repo folder.

## 4. Database Configuration

### 4.1 SQLite deployment

SQLite is acceptable for small portfolio sites. Keep the file in your project folder on PythonAnywhere.

### 4.2 Run migrations

In PythonAnywhere Bash:

```bash
cd ~/ <repo-name>
source ~/myportfolio-venv/bin/activate
python manage.py migrate
```

### 4.3 Create a superuser

```bash
python manage.py createsuperuser
```

### 4.4 Access the Django admin

Visit:

```text
https://yourusername.pythonanywhere.com/admin/
```

Log in with the superuser account.

## 5. Static and Media Files

### 5.1 Collect static files

```bash
python manage.py collectstatic --noinput
```

### 5.2 Configure static file mapping on PythonAnywhere

In the **Web** tab, add a Static files mapping:

- URL: `/static/`
- Path: `/home/yourusername/<repo-name>/staticfiles`

### 5.3 Configure media file mapping

Also add:

- URL: `/media/`
- Path: `/home/yourusername/<repo-name>/media`

## 6. Security Configuration

### 6.1 CSRF and session security

Add these production settings in `myportfolio/settings.py`:

```python
SESSION_COOKIE_SECURE = os.getenv("DJANGO_SESSION_COOKIE_SECURE", "False").lower() in ("1", "true", "yes")
CSRF_COOKIE_SECURE = os.getenv("DJANGO_CSRF_COOKIE_SECURE", "False").lower() in ("1", "true", "yes")
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
```

### 6.2 Optional HTTPS settings

If HTTPS is enabled on PythonAnywhere:

```python
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
```

> For a free account, do not enable `SECURE_SSL_REDIRECT` until HTTPS is confirmed working.

### 6.3 Best security practices

- Never commit your real `SECRET_KEY`.
- Keep `DEBUG=False` in production.
- Keep `.env` out of Git.
- Use environment variables for secrets.

## 7. Domain Configuration

### 7.1 PythonAnywhere subdomain

Your site is available at:

```text
https://yourusername.pythonanywhere.com
```

### 7.2 Custom domain setup (optional)

For paid accounts:
1. Set your custom domain in the PythonAnywhere Web tab.
2. Add a CNAME record from your domain to `yourusername.pythonanywhere.com`.
3. Add the custom domain to `ALLOWED_HOSTS`.

Example:

```python
ALLOWED_HOSTS = [
    "yourusername.pythonanywhere.com",
    "www.yourdomain.com",
    "yourdomain.com",
]
```

## 8. Deployment Testing

### 8.1 Homepage testing

Visit your URL and verify:
- page loads successfully
- CSS and JS appear
- navigation links work

### 8.2 Contact form testing

Submit the form and verify:
- validation works
- success message appears
- form data saves or sends email as expected

### 8.3 Admin panel testing

Open `/admin/` and verify login.

### 8.4 Media upload testing

Upload a file or image if supported and verify it loads from `/media/`.

## 9. Common Errors and Fixes

### 9.1 `400 Bad Request`

Cause: invalid `ALLOWED_HOSTS`.
Fix: add your host to `ALLOWED_HOSTS`.

### 9.2 `403 Forbidden`

Cause: missing CSRF origins or cookie settings.
Fix:

```python
CSRF_TRUSTED_ORIGINS = ["https://yourusername.pythonanywhere.com"]
```

### 9.3 `404 Not Found`

Cause: static or media mapping broken.
Fix: ensure `/static/` and `/media/` mappings are correct.

### 9.4 `500 Internal Server Error`

Cause: application error or import problem.
Fix: inspect the PythonAnywhere error log and verify WSGI.

### 9.5 Static files not loading

Fix:
- run `python manage.py collectstatic --noinput`
- confirm `/static/` mapping points to `staticfiles`

### 9.6 Media files not displaying

Fix:
- confirm `/media/` mapping
- confirm `MEDIA_ROOT` and `MEDIA_URL`

### 9.7 WSGI issues

Fix:
- verify `DJANGO_SETTINGS_MODULE`
- verify project path and virtualenv in the Web tab

## 10. Maintenance

### 10.1 Pull updates from GitHub

```bash
cd ~/ <repo-name>
source ~/myportfolio-venv/bin/activate
git pull origin main
```

### 10.2 Run migrations after updates

```bash
python manage.py migrate
```

### 10.3 Restart the web app

In PythonAnywhere Web tab, click **Reload**.

### 10.4 Backups

- Keep code in GitHub
- Download `db.sqlite3` periodically
- Back up `media/`

## Useful commands summary

```bash
# local setup
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip freeze > requirements.txt

# PythonAnywhere setup
python3.12 -m venv myportfolio-venv
source myportfolio-venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```
