import pytest
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_logout_blacklists_refresh(authenticated_client):
    user, client = authenticated_client()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    resp = client.post('/api/v1/auth/logout/', {'refresh': str(refresh)}, format='json')
    assert resp.status_code == 204

    # second use should fail
    resp2 = client.post('/api/v1/auth/refresh/', {'refresh': str(refresh)}, format='json')
    assert resp2.status_code == 401
