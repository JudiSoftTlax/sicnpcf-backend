from rest_framework.test import APIClient


def test_schema_includes_manual_audit_endpoint():
    client = APIClient()
    resp = client.get('/api/v1/schema/')
    content = resp.content.decode()
    assert '/api/v1/audit/' in content
    assert '/api/v1/firma/sign' in content
    assert '/api/v1/documents/' in content


def test_schema_includes_auto_login_endpoint():
    client = APIClient()
    resp = client.get('/api/v1/schema/')
    content = resp.content.decode()
    assert '/api/v1/auth/login' in content
