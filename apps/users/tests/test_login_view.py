import pytest

from apps.users.tests.factories import UserFactory


@pytest.fixture
def juez(db):
    return UserFactory(email='juez1@pjet.gob.mx', password='Demo!2026')


@pytest.mark.django_db
def test_login_returns_access_and_refresh(juez, api_client):
    resp = api_client.post('/api/v1/auth/login/', {
        'email': 'juez1@pjet.gob.mx',
        'password': 'Demo!2026',
    }, format='json')
    assert resp.status_code == 200
    assert 'access' in resp.json()
    assert 'refresh' in resp.json()


@pytest.mark.django_db
def test_login_rejects_bad_password(juez, api_client):
    resp = api_client.post('/api/v1/auth/login/', {
        'email': 'juez1@pjet.gob.mx',
        'password': 'wrong',
    }, format='json')
    assert resp.status_code == 401


@pytest.mark.django_db
def test_login_rejects_unknown_email(api_client):
    resp = api_client.post('/api/v1/auth/login/', {
        'email': 'nobody@pjet.gob.mx',
        'password': 'x',
    }, format='json')
    assert resp.status_code == 401


@pytest.mark.django_db
def test_login_missing_email_returns_400(api_client):
    resp = api_client.post('/api/v1/auth/login/', {'password': 'x'}, format='json')
    assert resp.status_code == 400
    assert 'email' in resp.json()


@pytest.mark.django_db
def test_login_missing_password_returns_400(api_client):
    resp = api_client.post('/api/v1/auth/login/', {'email': 'x@y.mx'}, format='json')
    assert resp.status_code == 400
    assert 'password' in resp.json()


@pytest.mark.django_db
def test_login_invalid_email_format_returns_400(api_client):
    resp = api_client.post('/api/v1/auth/login/', {
        'email': 'not-an-email', 'password': 'x',
    }, format='json')
    assert resp.status_code == 400
    assert 'email' in resp.json()
