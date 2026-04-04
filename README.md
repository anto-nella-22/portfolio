# Antonella Lopez Portfolio

A Django-based developer portfolio and landing page for showcasing technical skills, featured projects, testimonials, and a contact workflow.

## Overview

This project is a personal portfolio site built with:

- Django
- Bootstrap 5
- Custom CSS and JavaScript
- PostgreSQL-compatible database configuration
- WhiteNoise for static asset serving
- Gunicorn for production serving

The site includes:

- A responsive landing page
- Theme toggle with light/dark support
- Skills grouped by category
- Projects and testimonials sections
- Contact form with Django messages
- SEO meta tags and `sitemap.xml`

## Features

- Responsive navigation with desktop and collapsed-menu interactions
- Custom design system and polished UI states
- Skills rendered from Django models
- Project cards with tech stack badges
- Toast notifications for contact-form feedback
- Search-engine-friendly meta tags
- Production-ready settings for Railway deployment

## Project Structure

```text
portfolio/
├── core/
│   ├── admin.py
│   ├── models.py
│   ├── sitemaps.py
│   ├── templates/core/
│   │   ├── base.html
│   │   └── home.html
│   └── views.py
├── portfolio/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── DESIGN.md
├── Procfile
├── README.md
├── manage.py
└── requirements.txt
```

## Requirements

- Python 3.10+
- PostgreSQL
- pip
- virtual environment support

## Local Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Create a local `.env` file from `.env.example`.
5. Run migrations.
6. Start the development server.

Example:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## Environment Variables

Use `.env.example` as your reference.

Core variables:

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `SITE_URL`
- `DEFAULT_FROM_EMAIL`
- `CONTACT_EMAIL`

Optional email variables:

- `EMAIL_BACKEND`
- `EMAIL_HOST`
- `EMAIL_PORT`
- `EMAIL_USE_TLS`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`

## Running Locally

After setup:

```bash
python manage.py runserver
```

App URLs:

- Home: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`
- Sitemap: `http://127.0.0.1:8000/sitemap.xml`

## Admin Content Management

The site content is powered by Django admin.

Models available in admin:

- `Skill`
- `Project`
- `Testimonial`

Create an admin user:

```bash
python manage.py createsuperuser
```

### Skills

Each skill includes:

- `name`
- `level`
- `icon`

The UI maps numeric `level` values to labels:

- `90+` → `Expert`
- `80+` → `Advanced`
- `70+` → `Strong`
- `60+` → `Proficient`
- below `60` → `Working Knowledge`

Skills are grouped automatically into categories like:

- Backend
- Frontend
- Databases
- DevOps & Deployment
- Workflow & Collaboration

### Projects

Each project includes:

- `title`
- `description`
- `tech_stack`
- `live_url`
- `github_url`
- `image`

Use comma-separated values for `tech_stack`, for example:

```text
Django, Python, PostgreSQL, Nginx, Gunicorn, Bootstrap
```

### Testimonials

Each testimonial includes:

- `name`
- `role`
- `text`
- `photo_url`

## Static and Media Files

- Static files are served through WhiteNoise in production.
- Uploaded media files are stored in `media/`.

For production, make sure your hosting setup supports persistent media storage if you plan to upload images through admin.

## SEO

The project includes:

- shared SEO meta blocks in `base.html`
- page-specific metadata in `home.html`
- `sitemap.xml`

If deploying publicly, set:

- `SITE_URL=https://your-domain.com`

## Railway Deployment

This project is prepared for Railway with:

- Gunicorn in `Procfile`
- WhiteNoise static serving
- env-driven production settings
- `runtime.txt` pinning Python 3.12 for dependency compatibility

Recommended Railway environment variables:

```env
DEBUG=False
SECRET_KEY=your-production-secret
ALLOWED_HOSTS=your-app.up.railway.app,your-domain.com
CSRF_TRUSTED_ORIGINS=https://your-app.up.railway.app,https://your-domain.com
SITE_URL=https://your-domain.com
DATABASE_URL=postgresql://...
DEFAULT_FROM_EMAIL=noreply@your-domain.com
CONTACT_EMAIL=your@email.com
```

If using SMTP:

```env
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-user
EMAIL_HOST_PASSWORD=your-password
```

### Deployment Checklist

Before or after deploying:

1. Set production environment variables in Railway.
2. Run migrations.
3. Run collectstatic.
4. Create a superuser if needed.
5. Verify `/sitemap.xml`.
6. Test the contact form.
7. Confirm images load correctly.

Useful commands:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

## Design Notes

The visual direction and design system ideas are documented in:

- [DESIGN.md](/home/antonella/projects/portfolio/DESIGN.md)

## Known Notes

- Media storage is local by default.
- Contact form email delivery depends on your configured email backend.
- Skill grouping is currently inferred from skill names in the view layer.

## Future Improvements

- Add explicit skill categories in the database
- Add `robots.txt`
- Add richer Open Graph image support
- Add automated tests for views and deployment-sensitive behavior
- Add persistent cloud media storage for production
