from pathlib import Path
import os

# Ścieżka bazowa projektu
BASE_DIR = Path(__file__).resolve().parent.parent

# Ustawienia testów
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Ścieżki przekierowań logowania
LOGIN_URL = "/users/login/"
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Klucz sekretu — nie używaj w produkcji!
SECRET_KEY = 'django-insecure-n8b#qn96)c#wptvxskg1d-3^6it)d2dd=r!huy^#cjtg)%!tz('

# Debug tylko w developmencie
DEBUG = True

ALLOWED_HOSTS = []

# Aplikacje zainstalowane
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crud',
]

# Backend autoryzacji
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Główny plik urls.py
ROOT_URLCONF = 'django_crud.urls'

# Szablony HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'django_crud.wsgi.application'

# Baza danych — PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_crud_db',
        'USER': 'django_user',
        'PASSWORD': 'dupa123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Walidacja haseł
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Ustawienia językowe i czasu
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Ścieżka do statycznych plików (CSS, JS)
STATIC_URL = '/static/'

# Pliki multimedialne (np. zdjęcia)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Domyślny typ klucza głównego
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
