# My Portfolio

A production-ready personal portfolio website built with Django 5, Bootstrap 5, HTML, CSS, and JavaScript.

## Features

- Home and About pages
- Projects app with list, detail, search, technology filtering, and pagination
- Blog app with listing, detail, SEO-friendly slugs, and rich HTML content
- Contact app with form validation, database persistence, and email notifications
- Resume upload and download
- Dark mode toggle, progress bars, testimonials, smooth animations, responsive UI
- Admin dashboard customization

## Setup

1. Create a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` and update values.
3. Run migrations:

```powershell
python manage.py migrate
```

4. Create a superuser:

```powershell
python manage.py createsuperuser
```

5. Start the development server:

```powershell
python manage.py runserver
```

## GitHub Deployment Prep

1. Create a repository on GitHub under `https://github.com/Alexdoned`.
2. Add the remote in your project:

```powershell
git remote add origin https://github.com/Alexdoned/My-portfolio.git
git branch -M main
git push -u origin main
```

3. If you choose a different repo name, replace `My-portfolio.git` with your actual repository name.

## Production Notes

- Configure `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, and `DJANGO_ALLOWED_HOSTS`
- Use `collectstatic` to gather static files
- Configure a real email backend in `.env`
- For MySQL, update `DATABASES` in `myportfolio/settings.py` as documented below.

## Deployment Guide

See `DEPLOYMENT.md` for a step-by-step PythonAnywhere deployment guide, environment variable setup, static/media mapping, and troubleshooting tips.

## CI Workflow

A GitHub Actions workflow has been added at `.github/workflows/django-ci.yml` to run Django checks, migration validation, and `collectstatic` on pushes and pull requests to `main`.
