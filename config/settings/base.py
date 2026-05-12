"""Base settings — shared across all environments."""
from datetime import timedelta
from pathlib import Path

from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DJANGO_DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=Csv())

LOCAL_APPS = [
    'apps.core',
    'apps.users',
    'apps.audit',
    'apps.documents',
    'apps.firma',
    'apps.oficialia',
    'apps.expediente',
    'apps.turnado',
    'apps.audiencias',
    'apps.notificaciones',
    'apps.exhortos',
    'apps.juicios_esp',
    'apps.registros',
    'apps.juicio_linea',
    'apps.tribunal_2a',
    'apps.estadistica',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_spectacular',
    'corsheaders',
    'guardian',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]},
}]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='sicnpcf'),
        'USER': config('DB_USER', default='sicnpcf'),
        'PASSWORD': config('DB_PASSWORD', default='sicnpcf_local'),
        'HOST': config('DB_HOST', default='postgres'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'apps.core.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 25,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=8),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}

CORS_ALLOWED_ORIGINS = config(
    'CORS_ALLOWED_ORIGINS',
    default='http://localhost:5173,http://localhost:5174,http://localhost:5175,http://localhost:5176',
    cast=Csv(),
)

AUTH_BACKEND = config('AUTH_BACKEND', default='local')
FIRMA_AUTHORITY = config('FIRMA_AUTHORITY', default='stub')
FIRMA_TSA = config('FIRMA_TSA', default='internal')
SALAS_BACKEND = config('SALAS_BACKEND', default='mock')
EMAIL_BACKEND_TOGGLE = config('EMAIL_BACKEND_TOGGLE', default='smtp')
SMS_BACKEND = config('SMS_BACKEND', default='console')
FEDERACION_BACKEND = config('FEDERACION_BACKEND', default='local')
REQUIRE_MFA_ROLES = config('REQUIRE_MFA_ROLES', default='admin_tic', cast=Csv())
AUDIT_HASH_SECRET = config('AUDIT_HASH_SECRET')

AUTH_USER_MODEL = 'users.User'

SPECTACULAR_SETTINGS = {
    'TITLE': 'SICNPCF API',
    'DESCRIPTION': 'Sistema Integral CNPCyF — Poder Judicial Tlaxcala',
    'VERSION': '0.1.0',
    'SERVE_INCLUDE_SCHEMA': False,
    'CONTACT': {'name': 'SINERGIA SICNPCF Team'},
    'LICENSE': {'name': 'PJET cesion derechos'},
}

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'guardian.backends.ObjectPermissionBackend',
]

# Disable guardian anonymous user — our User requires a Rol FK
ANONYMOUS_USER_NAME = None
