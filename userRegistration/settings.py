"""
Django settings for userRegistration project.

Generated by 'django-admin startproject' using Django 5.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os
TEMPLATES_DIR=os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nbf!byzcf-_wa_1@27p0g%q*=cdj&z@l412!dtar%=m+hrmwz&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles','app1',
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

ROOT_URLCONF = 'userRegistration.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'userRegistration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#By default we don't had registration for media ,--- we need to create it example(STATIC_URL = 'static/')


MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

EMAIL_HOST = 'smtp.gmail.com' #first of all it is a portal---SMTP (Simple Mail Transfer Protocol)which is used to send emails.
EMAIL_HOST_USER = 'kayamvamsikrishna@gmail.com'
EMAIL_HOST_PASSWORD = 'iovt qnwe igzc zibp'
EMAIL_PORT = 587 #Port 587 is the standard port for sending email securely using TLS.
EMAIL_USE_SSL = False

'''
WHY  EMAIL_USE_SSL = False ?

SSL (Secure Sockets Layer) is an older security protocol.
Here, it's set to False because we're using TLS instead, which is newer and more secure.

'''

EMAIL_USE_TLS = True
'''
WHY  EMAIL_USE_TLS = True?

TLS (Transport Layer Security) encrypts the email messages.

It's set to True to enable encryption, ensuring secure email transmission.

This works with port 587.
'''



'''
note point : 
IF I EMAIL_USE_SSL = TRUE THEN THE PORT NUMBER IS 465

EMAIL_PORT = 465


1)MAIN POINT DON'T USE BOTH SECURITY PROTOCOLS AT THE SAME TIME--- USE SSL OR TLS--- USE ANY ONE SECURITY PROTOCOL.

2)Use either TLS (587) or SSL (465), not both at the same time---- USE ANY ONE PORT NUMBER.


'''





