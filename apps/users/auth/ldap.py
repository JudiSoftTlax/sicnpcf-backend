from typing import Optional

from apps.users.auth.interfaces import IInstitutionalDirectory


class LdapDirectory(IInstitutionalDirectory):
    """AUTH_BACKEND=ldap. Placeholder hasta resolver P-001.

    Cuando PJET confirme AD/LDAP, se inyectan host/baseDN/bindDN via settings
    y se implementa con python-ldap o ldap3.
    """

    def authenticate(self, *, email: str, password: str) -> Optional['User']:  # noqa: F821
        raise NotImplementedError('LDAP backend pendiente de P-001')
