from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from apps.core.models import Organo, Rol
from apps.core.models.mixins import SoftDeleteModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, SoftDeleteModel):
    email = models.EmailField(unique=True)
    curp = models.CharField(max_length=18, unique=True, null=True, blank=True)
    organo = models.ForeignKey(Organo, on_delete=models.PROTECT, null=True, blank=True,
                                related_name='usuarios')
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, related_name='usuarios')
    institution_id = models.CharField(max_length=50, blank=True, default='')
    mfa_enabled = models.BooleanField(default=False)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()  # type: ignore[misc, assignment]

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email
