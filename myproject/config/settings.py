"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# django 폴더를 뜻함
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 'django/templates'폴더
TEMPLATES_DIR = os.path.join(BASE_DIR, tem)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nra6$a&om_8e6x7p_p37enn#8f7=+1^m45s5davyf$)g!h)&_n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.contrib.admin',
    'blog.contrib.auth',
    'blog.contrib.contenttypes',
    'blog.contrib.sessions',
    'blog.contrib.messages',
    'blog.contrib.staticfiles',

    'blog', #django 추가
]

MIDDLEWARE = [
    'blog.middleware.security.SecurityMiddleware',
    'blog.contrib.sessions.middleware.SessionMiddleware',
    'blog.middleware.common.CommonMiddleware',
    'blog.middleware.csrf.CsrfViewMiddleware',
    'blog.contrib.auth.middleware.AuthenticationMiddleware',
    'blog.contrib.messages.middleware.MessageMiddleware',
    'blog.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # django에서 템플리을 검색할 경로 목적
        'DIRS': [
            TEMPLATES_DIR,
        ],
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


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'blog.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'blog.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'blog.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'blog.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'blog.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
