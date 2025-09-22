from pathlib import Path
import os
import dj_database_url  # for PostgreSQL on Render

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv('SECRET_KEY', 'dummy-fallback-secret')  # set SECRET_KEY on Render
DEBUG = False  # Production

# Allowed hosts
ALLOWED_HOSTS = [
    'django-notifications-audit-3.onrender.com',  # your Render domain
]

# Optional: Load extra hosts from environment variable
extra_hosts = os.getenv("ALLOWED_HOSTS")
if extra_hosts:
    ALLOWED_HOSTS.extend(extra_hosts.split(","))

# CSRF trusted origins (important for Render HTTPS)
CSRF_TRUSTED_ORIGINS = [
    'https://django-notifications-audit-3.onrender.com'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notifications',
    'audit_logs',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_notifications_audit.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add templates directories if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_notifications_audit.wsgi.application'

# Database configuration: PostgreSQL on Render or fallback to SQLite
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600,
        ssl_require=True  # required for PostgreSQL on Render
    )
}

# Password validation
AUTH_PASSWORD_VALIDATORS = []

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # collectstatic will use this

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
