def test_schema_endpoint_returns_openapi():
    from rest_framework.test import APIClient
    client = APIClient()
    resp = client.get('/api/v1/schema/')
    assert resp.status_code == 200
    assert 'openapi' in resp.content.decode()
