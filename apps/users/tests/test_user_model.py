import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from apps.core.models import Organo, Rol


@pytest.mark.django_db
def test_create_user_with_email_curp_organo_rol():
    user = get_user_model()
    organo = Organo.objects.create(clave='JF-01', nombre='Juz Fam 1',
                                    distrito='Tlx', materia='familiar')
    rol = Rol.objects.create(slug='juez', nombre='Juez', portal='interno')
    u = user.objects.create_user(
        email='juez1@pjet.gob.mx',
        password='Demo!2026',
        curp='HEGJ800101HTLRZN09',
        organo=organo,
        rol=rol,
    )
    assert u.email == 'juez1@pjet.gob.mx'
    assert u.curp == 'HEGJ800101HTLRZN09'
    assert u.organo == organo
    assert u.rol == rol
    assert u.check_password('Demo!2026')


@pytest.mark.django_db
def test_email_must_be_unique():
    user = get_user_model()
    rol = Rol.objects.create(slug='ciudadano', nombre='Ciudadano', portal='ciudadano')
    user.objects.create_user(email='same@x.mx', password='x', rol=rol)
    with pytest.raises(IntegrityError):
        user.objects.create_user(email='same@x.mx', password='x', rol=rol)


@pytest.mark.django_db
def test_curp_must_be_18_chars_or_null():
    user = get_user_model()
    rol = Rol.objects.create(slug='ciudadano', nombre='Ciudadano', portal='ciudadano')
    u = user.objects.create_user(email='nocurp@x.mx', password='x', rol=rol)
    assert u.curp is None
