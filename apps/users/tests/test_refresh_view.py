import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.core.models import Rol


@pytest.fixture
def juez(db):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    rol = Rol.objects.create(slug='juez', nombre='Juez', portal='interno')
    return User.objects.create_user(email='juez1@pjet.gob.mx', password='Demo!2026', rol=rol)


@pytest.mark.django_db
def test_refresh_returns_new_access(juez):
    refresh = RefreshToken.for_user(juez)
    client = APIClient()
    resp = client.post('/api/v1/auth/refresh', {'refresh': str(refresh)}, format='json')
    assert resp.status_code == 200
    assert 'access' in resp.json()


@pytest.mark.django_db
def test_refresh_rejects_invalid_token():
    client = APIClient()
    resp = client.post('/api/v1/auth/refresh', {'refresh': 'garbage'}, format='json')
    assert resp.status_code == 401
