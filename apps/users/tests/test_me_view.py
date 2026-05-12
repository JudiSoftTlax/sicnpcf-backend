import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.core.models import Organo, Rol


@pytest.fixture
def juez(db):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    organo = Organo.objects.create(clave='JF-01', nombre='Juz Fam 1',
                                    distrito='Tlx', materia='familiar')
    rol = Rol.objects.create(slug='juez', nombre='Juez', portal='interno')
    return User.objects.create_user(
        email='juez1@pjet.gob.mx', password='Demo!2026',
        organo=organo, rol=rol,
        first_name='Ana', last_name='Pérez',
    )


@pytest.mark.django_db
def test_me_returns_user_profile(juez):
    client = APIClient()
    token = RefreshToken.for_user(juez).access_token
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    resp = client.get('/api/v1/users/me')
    assert resp.status_code == 200
    data = resp.json()
    assert data['email'] == 'juez1@pjet.gob.mx'
    assert data['first_name'] == 'Ana'
    assert data['rol']['slug'] == 'juez'
    assert data['organo']['clave'] == 'JF-01'


@pytest.mark.django_db
def test_me_unauthenticated_returns_401():
    client = APIClient()
    resp = client.get('/api/v1/users/me')
    assert resp.status_code == 401
