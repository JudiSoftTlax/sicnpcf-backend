import pytest


@pytest.mark.django_db
def test_me_returns_user_profile(authenticated_client):
    user, client = authenticated_client(
        role_slug='juez',
        email='juez1@pjet.gob.mx',
        first_name='Ana',
        last_name='Pérez',
    )
    resp = client.get('/api/v1/users/me/')
    assert resp.status_code == 200
    data = resp.json()
    assert data['email'] == 'juez1@pjet.gob.mx'
    assert data['first_name'] == 'Ana'
    assert data['rol']['slug'] == 'juez'
    assert data['organo']['clave'] == 'JF-01'


@pytest.mark.django_db
def test_me_unauthenticated_returns_401(api_client):
    resp = api_client.get('/api/v1/users/me/')
    assert resp.status_code == 401
