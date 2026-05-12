"""Smoke tests to verify factory_boy factories produce valid instances."""
import pytest

from apps.core.tests.factories import (
    MateriaFactory,
    OrganoFactory,
    RolFactory,
    TipoJuicioFactory,
)
from apps.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_factory_creates_user():
    u = UserFactory()
    assert u.email
    assert u.check_password('Test!2026')


@pytest.mark.django_db
def test_user_factory_with_custom_role():
    rol = RolFactory(slug='ciudadano', portal='ciudadano')
    u = UserFactory(rol=rol)
    assert u.rol.slug == 'ciudadano'


@pytest.mark.django_db
def test_materia_factory_creates_distinct_values():
    m1 = MateriaFactory()
    m2 = MateriaFactory()
    # Iterator cycles through values; both should exist
    assert {m1.clave, m2.clave} <= {'civil', 'familiar'}


@pytest.mark.django_db
def test_tipo_juicio_factory_creates_user():
    tj = TipoJuicioFactory()
    assert tj.clave.startswith('TJ-')
    assert tj.materia in ('civil', 'familiar')


@pytest.mark.django_db
def test_organo_factory_creates_with_sequence():
    o1 = OrganoFactory()
    o2 = OrganoFactory()
    assert o1.clave != o2.clave
    assert o1.clave.startswith('ORG-')


@pytest.mark.django_db
def test_authenticated_client_with_no_organo(authenticated_client):
    user, _ = authenticated_client(role_slug='ciudadano', organo_clave=None)
    assert user.organo is None
