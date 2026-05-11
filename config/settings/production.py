"""Produccion — servidor PJET."""
from .base import *  # noqa
import dj_database_url

DATABASES = {'default': dj_database_url.config()}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
