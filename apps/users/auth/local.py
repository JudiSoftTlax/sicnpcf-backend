from typing import Optional

from django.contrib.auth import authenticate as django_authenticate
from django.contrib.auth import get_user_model

from apps.users.auth.interfaces import IInstitutionalDirectory

User = get_user_model()


class LocalDirectory(IInstitutionalDirectory):
    """AUTH_BACKEND=local. Valida contra la tabla `users.User` de Django."""

    def authenticate(self, *, email: str, password: str) -> Optional['User']:
        return django_authenticate(username=email, password=password)
