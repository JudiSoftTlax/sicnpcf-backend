from __future__ import annotations

from typing import TYPE_CHECKING

from apps.users.auth.interfaces import IInstitutionalDirectory

if TYPE_CHECKING:
    from apps.users.models import User


class LdapDirectory(IInstitutionalDirectory):
    """AUTH_BACKEND=ldap. Placeholder hasta resolver P-001.

    Cuando PJET confirme AD/LDAP, se inyectan host/baseDN/bindDN via settings
    y se implementa con python-ldap o ldap3.
    """

    def authenticate(self, *, email: str, password: str) -> User | None:
        raise NotImplementedError('LDAP backend pendiente de P-001')
