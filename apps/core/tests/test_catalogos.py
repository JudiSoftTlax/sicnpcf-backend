import pytest
from django.db import IntegrityError

from apps.core.models import Materia, Organo, Rol, TipoJuicio


@pytest.mark.django_db
def test_organo_str():
    o = Organo.objects.create(
        clave='JF-01',
        nombre='Juzgado Familiar 1',
        distrito='Tlaxcala',
        materia='familiar',
    )
    assert str(o) == 'JF-01 — Juzgado Familiar 1'


@pytest.mark.django_db
def test_tipo_juicio_unique_clave():
    TipoJuicio.objects.create(clave='ORAL-CIV', nombre='Oral civil', materia='civil')
    with pytest.raises(IntegrityError):
        TipoJuicio.objects.create(clave='ORAL-CIV', nombre='Otro', materia='familiar')


@pytest.mark.django_db
def test_rol_slug_unique():
    Rol.objects.create(slug='juez', nombre='Juez', portal='interno')
    with pytest.raises(IntegrityError):
        Rol.objects.create(slug='juez', nombre='Otro Juez', portal='interno')


@pytest.mark.django_db
def test_materia_choices():
    m = Materia.objects.create(clave='civil', nombre='Civil')
    assert m.clave == 'civil'
