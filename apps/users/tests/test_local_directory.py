import pytest
from django.contrib.auth import get_user_model

from apps.core.models import Rol
from apps.users.auth.local import LocalDirectory

User = get_user_model()


@pytest.mark.django_db
def test_local_directory_authenticate_success():
    rol = Rol.objects.create(slug='ciudadano', nombre='Ciudadano', portal='ciudadano')
    User.objects.create_user(email='alice@x.mx', password='Demo!2026', rol=rol)
    directory = LocalDirectory()
    result = directory.authenticate(email='alice@x.mx', password='Demo!2026')
    assert result is not None
    assert result.email == 'alice@x.mx'


@pytest.mark.django_db
def test_local_directory_authenticate_bad_password():
    rol = Rol.objects.create(slug='ciudadano', nombre='Ciudadano', portal='ciudadano')
    User.objects.create_user(email='alice@x.mx', password='Demo!2026', rol=rol)
    directory = LocalDirectory()
    assert directory.authenticate(email='alice@x.mx', password='wrong') is None


@pytest.mark.django_db
def test_local_directory_authenticate_unknown_email():
    directory = LocalDirectory()
    assert directory.authenticate(email='nobody@x.mx', password='x') is None
