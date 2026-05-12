from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.auth import get_directory


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    totp = serializers.CharField(required=False, allow_blank=True)

    def validate(self, attrs):
        directory = get_directory()
        user = directory.authenticate(email=attrs['email'], password=attrs['password'])
        if user is None or not user.is_active:
            raise serializers.ValidationError('Credenciales inválidas', code='invalid')
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class OrganoBriefSerializer(serializers.Serializer):
    clave = serializers.CharField()
    nombre = serializers.CharField()
    distrito = serializers.CharField()
    materia = serializers.CharField()


class RolBriefSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    nombre = serializers.CharField()
    portal = serializers.CharField()


class UserMeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    curp = serializers.CharField(allow_null=True)
    institution_id = serializers.CharField(allow_null=True)
    mfa_enabled = serializers.BooleanField()
    organo = OrganoBriefSerializer(allow_null=True)
    rol = RolBriefSerializer()
