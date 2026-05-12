import pytest
from rest_framework.test import APIClient

from apps.core.models import Rol


@pytest.fixture
def juez(db):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    rol = Rol.objects.create(slug='juez', nombre='Juez', portal='interno')
    return User.objects.create_user(email='juez1@pjet.gob.mx', password='Demo!2026', rol=rol)


@pytest.mark.django_db
def test_login_returns_access_and_refresh(juez):
    client = APIClient()
    resp = client.post('/api/v1/auth/login', {
        'email': 'juez1@pjet.gob.mx',
        'password': 'Demo!2026',
    }, format='json')
    assert resp.status_code == 200
    assert 'access' in resp.json()
    assert 'refresh' in resp.json()


@pytest.mark.django_db
def test_login_rejects_bad_password(juez):
    client = APIClient()
    resp = client.post('/api/v1/auth/login', {
        'email': 'juez1@pjet.gob.mx',
        'password': 'wrong',
    }, format='json')
    assert resp.status_code == 401


@pytest.mark.django_db
def test_login_rejects_unknown_email():
    client = APIClient()
    resp = client.post('/api/v1/auth/login', {
        'email': 'nobody@pjet.gob.mx',
        'password': 'x',
    }, format='json')
    assert resp.status_code == 401
