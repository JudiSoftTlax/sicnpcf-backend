from django.db import models

from apps.core.models.mixins import SoftDeleteModel, TimeStampedModel

MATERIA_CHOICES = [
    ('civil', 'Civil'),
    ('familiar', 'Familiar'),
]

PORTAL_CHOICES = [
    ('ciudadano', 'Ciudadano'),
    ('interno', 'Interno'),
    ('admin', 'Admin'),
    ('interinst', 'Interinstitucional'),
]


class Materia(TimeStampedModel, SoftDeleteModel):
    clave = models.CharField(max_length=20, unique=True, choices=MATERIA_CHOICES)
    nombre = models.CharField(max_length=64)

    class Meta:
        ordering = ['clave']

    def __str__(self):
        return self.nombre


class Organo(TimeStampedModel, SoftDeleteModel):
    clave = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=200)
    distrito = models.CharField(max_length=100)
    materia = models.CharField(max_length=20, choices=MATERIA_CHOICES)
    direccion = models.TextField(blank=True)

    class Meta:
        ordering = ['clave']
        verbose_name_plural = 'Órganos'

    def __str__(self):
        return f'{self.clave} — {self.nombre}'


class TipoJuicio(TimeStampedModel, SoftDeleteModel):
    clave = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=200)
    materia = models.CharField(max_length=20, choices=MATERIA_CHOICES)
    es_especializado = models.BooleanField(default=False)

    class Meta:
        ordering = ['materia', 'nombre']
        verbose_name_plural = 'Tipos de juicio'

    def __str__(self):
        return f'{self.clave} — {self.nombre}'


class Rol(TimeStampedModel, SoftDeleteModel):
    slug = models.SlugField(max_length=40, unique=True)
    nombre = models.CharField(max_length=100)
    portal = models.CharField(max_length=20, choices=PORTAL_CHOICES)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ['slug']
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.nombre
