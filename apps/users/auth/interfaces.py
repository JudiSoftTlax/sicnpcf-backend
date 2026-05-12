from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apps.users.models import User


class IInstitutionalDirectory(ABC):
    """Source-of-truth para credenciales de usuarios.

    Swap-able via AUTH_BACKEND setting. P-001 abierta.
    """

    @abstractmethod
    def authenticate(self, *, email: str, password: str) -> User | None:
        """Devuelve el User si las credenciales son válidas, None si no."""
