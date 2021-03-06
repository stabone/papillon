"""
Django settings for papillon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '87&0q8^o*!eznt3%^1++)nqbyk)64(%t8p(*b-*s7j5ugmo5gn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/article/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls',
    'courses',
    'users',
    'helper',
    'comments',
    'messaging',
    'articles',
    'badges',
    'django_markdown',
    'categories',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'papillon.urls'

WSGI_APPLICATION = 'papillon.wsgi.application'

# template configuration
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': 'papillon',
        # 'USER': 'root',
        # 'PASSWORD': 'lamp',
        # 'HOST': '127.0.0.1',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'lv'

TIME_ZONE = 'Europe/Riga'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# more like hack becouse media_url isn't in loaded dir
# MEDIA_URL = '/media'
MEDIA_URL = '/static/media/'
# MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static/media')


# Email settings
# for now [python -m smtpd -n -c DebuggingServer localhost:1025]
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_POST_USER = 'ivars883@gmail.com'
EMAIL_HOST_PASSWORD = 'inbox.lv'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
