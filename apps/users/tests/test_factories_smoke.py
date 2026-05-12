"""Smoke tests to verify factory_boy factories produce valid instances."""
import pytest

from apps.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_factory_creates_user():
    u = UserFactory()
    assert u.email
    assert u.check_password('Test!2026')


@pytest.mark.django_db
def test_user_factory_with_custom_role():
    from apps.core.tests.factories import RolFactory

    rol = RolFactory(slug='ciudadano', portal='ciudadano')
    u = UserFactory(rol=rol)
    assert u.rol.slug == 'ciudadano'
