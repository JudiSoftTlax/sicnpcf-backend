from django.conf import settings

from apps.users.auth.interfaces import IInstitutionalDirectory
from apps.users.auth.ldap import LdapDirectory
from apps.users.auth.local import LocalDirectory


def get_directory() -> IInstitutionalDirectory:
    backend = settings.AUTH_BACKEND
    if backend == 'local':
        return LocalDirectory()
    if backend == 'ldap':
        return LdapDirectory()
    raise ValueError(f'AUTH_BACKEND inválido: {backend!r}')


__all__ = ['IInstitutionalDirectory', 'LocalDirectory', 'LdapDirectory', 'get_directory']
