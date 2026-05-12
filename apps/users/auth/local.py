from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth import authenticate as django_authenticate

from apps.users.auth.interfaces import IInstitutionalDirectory

if TYPE_CHECKING:
    from apps.users.models import User


class LocalDirectory(IInstitutionalDirectory):
    """AUTH_BACKEND=local. Valida contra la tabla `users.User` de Django."""

    def authenticate(self, *, email: str, password: str) -> User | None:
        return django_authenticate(username=email, password=password)  # type: ignore[return-value]
