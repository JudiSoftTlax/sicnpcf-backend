"""Tests for TimeStampedModel and SoftDeleteModel mixins.

Uses concrete catalog models (Organo, Rol) that inherit from these mixins,
since test-only in-memory models don't have DB tables.
"""
import pytest

from apps.core.models import Organo


@pytest.mark.django_db
def test_timestamped_sets_created_and_updated_at():
    obj = Organo.objects.create(clave='JF-01', nombre='Juzgado Familiar 1',
                                 distrito='Tlaxcala', materia='familiar')
    assert obj.created_at is not None
    assert obj.updated_at is not None


@pytest.mark.django_db
def test_soft_delete_hides_from_default_manager():
    obj = Organo.objects.create(clave='JC-02', nombre='Juzgado Civil 2',
                                 distrito='Tlaxcala', materia='civil')
    obj.delete()
    assert obj.deleted_at is not None
    assert Organo.objects.filter(pk=obj.pk).count() == 0
    assert Organo.all_objects.filter(pk=obj.pk).count() == 1
