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
def test_logout_blacklists_refresh(juez):
    refresh = RefreshToken.for_user(juez)
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    resp = client.post('/api/v1/auth/logout', {'refresh': str(refresh)}, format='json')
    assert resp.status_code == 204

    # second use should fail
    resp2 = client.post('/api/v1/auth/refresh', {'refresh': str(refresh)}, format='json')
    assert resp2.status_code == 401
