"""Local dev (`docker compose up`) and AWS Fargate dev environment."""
import os

import dj_database_url

from .base import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True

if os.environ.get('DATABASE_URL'):
    DATABASES = {'default': dj_database_url.config(conn_max_age=60)}
