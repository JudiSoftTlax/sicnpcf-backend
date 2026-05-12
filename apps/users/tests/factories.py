"""Factory-boy factories for User model."""
import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from apps.core.tests.factories import OrganoFactory, RolFactory

User = get_user_model()  # noqa: N806


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)

    email = factory.Sequence(lambda n: f'user{n:03d}@pjet.gob.mx')
    first_name = factory.Faker('first_name', locale='es_MX')
    last_name = factory.Faker('last_name', locale='es_MX')
    organo = factory.SubFactory(OrganoFactory)
    rol = factory.SubFactory(RolFactory)

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if not create:
            return
        self.set_password(extracted or 'Test!2026')
        self.save()
