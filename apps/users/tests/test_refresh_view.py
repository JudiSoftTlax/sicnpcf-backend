import pytest
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_refresh_returns_new_access(authenticated_client, api_client):
    user, _ = authenticated_client()
    refresh = RefreshToken.for_user(user)
    resp = api_client.post('/api/v1/auth/refresh/', {'refresh': str(refresh)}, format='json')
    assert resp.status_code == 200
    assert 'access' in resp.json()


@pytest.mark.django_db
def test_refresh_rejects_invalid_token(api_client):
    resp = api_client.post('/api/v1/auth/refresh/', {'refresh': 'garbage'}, format='json')
    assert resp.status_code == 401
