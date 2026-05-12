"""Tests for health endpoint."""
from django.test import Client


def test_health_returns_200_and_ok_payload():
    client = Client()
    response = client.get('/api/v1/health/')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'ok'
    assert 'version' in data
