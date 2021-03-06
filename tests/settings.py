# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "yg-_alcrywd7_f6q0%tlzg6zv=2=e=j=n-*x$*dwc(dcw*(=(0"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "signoff.apps.SignoffConfig",
]

SITE_ID = 1

MIDDLEWARE = (
    'signoff.middleware.ConsentMiddleware',
)
