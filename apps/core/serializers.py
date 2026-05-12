from rest_framework import serializers

from apps.core.models import Organo, TipoJuicio


class OrganoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organo
        fields = ['id', 'clave', 'nombre', 'distrito', 'materia', 'direccion']


class TipoJuicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoJuicio
        fields = ['id', 'clave', 'nombre', 'materia', 'es_especializado']
