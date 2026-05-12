import pytest
from rest_framework.test import APIClient

from apps.core.models import Organo, TipoJuicio


@pytest.mark.django_db
def test_organos_list_returns_active_organos():
    Organo.objects.create(clave='JF-01', nombre='Juz Fam 1', distrito='Tlx', materia='familiar')
    Organo.objects.create(clave='JC-02', nombre='Juz Civ 2', distrito='Tlx', materia='civil')
    client = APIClient()
    resp = client.get('/api/v1/core/organos/')
    assert resp.status_code == 200
    data = resp.json()
    assert data['count'] == 2
    assert any(o['clave'] == 'JF-01' for o in data['results'])


@pytest.mark.django_db
def test_organos_filter_by_materia():
    Organo.objects.create(clave='JF-01', nombre='Juz Fam 1', distrito='Tlx', materia='familiar')
    Organo.objects.create(clave='JC-02', nombre='Juz Civ 2', distrito='Tlx', materia='civil')
    client = APIClient()
    resp = client.get('/api/v1/core/organos/?materia=familiar')
    assert resp.json()['count'] == 1


@pytest.mark.django_db
def test_tipos_juicio_list():
    TipoJuicio.objects.create(clave='ORAL-CIV', nombre='Oral civil', materia='civil')
    client = APIClient()
    resp = client.get('/api/v1/core/tipos-juicio/')
    assert resp.status_code == 200
    assert resp.json()['count'] == 1
