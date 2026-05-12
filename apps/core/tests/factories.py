"""Factory-boy factories for core catalog models."""
import factory
from factory.django import DjangoModelFactory

from apps.core.models import Materia, Organo, Rol, TipoJuicio


class OrganoFactory(DjangoModelFactory):
    class Meta:
        model = Organo
        django_get_or_create = ('clave',)

    clave = factory.Sequence(lambda n: f'ORG-{n:03d}')
    nombre = factory.Faker('company', locale='es_MX')
    distrito = 'Tlaxcala'
    materia = 'familiar'


class TipoJuicioFactory(DjangoModelFactory):
    class Meta:
        model = TipoJuicio
        django_get_or_create = ('clave',)

    clave = factory.Sequence(lambda n: f'TJ-{n:03d}')
    nombre = factory.Faker('sentence', nb_words=4, locale='es_MX')
    materia = 'familiar'


class MateriaFactory(DjangoModelFactory):
    class Meta:
        model = Materia
        django_get_or_create = ('clave',)

    clave = factory.Iterator(['civil', 'familiar'])
    nombre = factory.LazyAttribute(lambda o: o.clave.title())


class RolFactory(DjangoModelFactory):
    class Meta:
        model = Rol
        django_get_or_create = ('slug',)

    slug = factory.Sequence(lambda n: f'rol-{n:03d}')
    nombre = factory.Faker('job', locale='es_MX')
    portal = 'interno'
