"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from datetime import timedelta
from pathlib import Path

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

DEBUG = env('DEBUG')

SETTINGS_DIR = Path(__file__).resolve().parent
CONFIG_BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# Take environment variables from .env file
environ.Env.read_env(os.path.join(SETTINGS_DIR, '.env'))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
    'apps.authentication',
    'apps.core',
    'apps.users',
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'apps.authentication.middleware.EnsureAuthenticatedMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apps.core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR.parent, 'static')

STATIC_URL = '/static/'

# Rutas adicionales para buscar archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR.parent, 'staticfiles'),
]

# Configuración de archivos multimedia (si aplica)
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

ACCESS_TOKEN_LIFETIME = env.int('ACCESS_TOKEN_LIFETIME', 5)
SLIDING_TOKEN_REFRESH_LIFETIME = env.int('SLIDING_TOKEN_REFRESH_LIFETIME', 1)
SLIDING_TOKEN_LIFETIME = env.int('SLIDING_TOKEN_LIFETIME', 1)
SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER = env.int('SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER', 1)
SLIDING_TOKEN_LIFETIME_LATE_USER = env.int('SLIDING_TOKEN_LIFETIME_LATE_USER', 1)
SIGNING_KEY = env('SECRET_KEY')

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=ACCESS_TOKEN_LIFETIME),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=SLIDING_TOKEN_REFRESH_LIFETIME),
    'SLIDING_TOKEN_LIFETIME': timedelta(days=SLIDING_TOKEN_LIFETIME),
    'SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER': timedelta(days=SLIDING_TOKEN_REFRESH_LIFETIME_LATE_USER),
    'SLIDING_TOKEN_LIFETIME_LATE_USER': timedelta(days=SLIDING_TOKEN_LIFETIME_LATE_USER),
    'TOKEN_OBTAIN_SERIALIZER': 'apps.authentication.serializers.CustomTokenObtainPairSerializer',
    'ISSUER': 'HMartinez',
    'AUDIENCE': 'BaseUsers',
    'SIGNING_KEY': SECRET_KEY,
    'USER_ID_FIELD': 'uuid',  # Usa 'uuid' como el campo de identificación del usuario
    'USER_ID_CLAIM': 'user_id',  # Usa 'user_id' como la clave del claim para el id del usuario
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Mi API Documentada',
    'DESCRIPTION': 'Documentación automática de mi API usando drf-spectacular',
    'VERSION': '1.0.0',
}
