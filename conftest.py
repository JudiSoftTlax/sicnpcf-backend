"""Fixtures globales del proyecto."""
import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.fixture
def api_client():
    """DRF APIClient sin autenticacion."""
    return APIClient()


@pytest.fixture
def authenticated_client(db, api_client):
    """Factory que crea un usuario con el rol pedido y devuelve un client autenticado.

    Usage::

        def test_something(authenticated_client):
            user, client = authenticated_client(role_slug='juez')
            resp = client.get('/api/v1/users/me/')

    Args:
        role_slug: slug del Rol a asignar (default 'juez').
        email: email del usuario; si None se genera como ``<role_slug>@test.mx``.
        organo_clave: clave del Organo a asignar; None para sin organo.
    """
    from django.contrib.auth import get_user_model

    from apps.core.models import Organo, Rol

    User = get_user_model()  # noqa: N806

    def _make(role_slug='juez', email=None, organo_clave='JF-01'):
        rol, _ = Rol.objects.get_or_create(
            slug=role_slug,
            defaults={'nombre': role_slug.title(), 'portal': 'interno'},
        )
        organo = None
        if organo_clave:
            organo, _ = Organo.objects.get_or_create(
                clave=organo_clave,
                defaults={'nombre': 'Test Organo', 'distrito': 'Tlx', 'materia': 'familiar'},
            )
        user = User.objects.create_user(
            email=email or f'{role_slug}@test.mx',
            password='Test!2026',
            rol=rol,
            organo=organo,
        )
        token = RefreshToken.for_user(user).access_token
        api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return user, api_client

    return _make
