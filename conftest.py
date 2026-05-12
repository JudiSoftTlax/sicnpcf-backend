"""Fixtures globales del proyecto."""
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    """DRF APIClient sin autenticación."""
    return APIClient()


@pytest.fixture
def authenticated_client(db, api_client):
    """Factory que crea un usuario con UserFactory y devuelve un client autenticado.

    Uso:
        user, client = authenticated_client()  # juez en JF-01
        user, client = authenticated_client(role_slug='ciudadano', organo_clave=None)
        user, client = authenticated_client(first_name='Ana', last_name='Pérez', curp='HEGJ800101...')

    Args:
        role_slug: slug del Rol a asignar (default: 'juez')
        organo_clave: clave del Organo, o None para usuarios sin órgano (ciudadanos)
        **user_kwargs: cualquier kwarg adicional pasado a UserFactory
                       (email, first_name, last_name, curp, institution_id, etc.)

    Nota: el JWT se mintea via `RefreshToken.for_user(user).access_token`, saltando
    el endpoint /auth/login. Para tests de integración con flujo completo de login,
    usar APIClient.post('/api/v1/auth/login/', ...) directamente.
    """
    from apps.core.tests.factories import OrganoFactory, RolFactory
    from apps.users.tests.factories import UserFactory

    def _make(*, role_slug='juez', organo_clave='JF-01', **user_kwargs):
        rol = RolFactory(slug=role_slug, portal='interno', nombre=role_slug.replace('_', ' ').title())
        organo = OrganoFactory(clave=organo_clave) if organo_clave else None
        user = UserFactory(rol=rol, organo=organo, **user_kwargs)
        token = RefreshToken.for_user(user).access_token
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return user, api_client

    return _make
