from abc import ABC, abstractmethod
from typing import Optional

from django.contrib.auth import get_user_model

User = get_user_model()


class IInstitutionalDirectory(ABC):
    """Source-of-truth para credenciales de usuarios.

    Swap-able via AUTH_BACKEND setting. P-001 abierta.
    """

    @abstractmethod
    def authenticate(self, *, email: str, password: str) -> Optional['User']:
        """Devuelve el User si las credenciales son válidas, None si no."""
