from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import LoginSerializer, UserMeSerializer


@extend_schema(
    request=LoginSerializer,
    responses={200: {'type': 'object', 'properties': {
        'access': {'type': 'string'}, 'refresh': {'type': 'string'}}}},
    tags=['auth'],
)
@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if not serializer.is_valid():
        raise AuthenticationFailed(detail=serializer.errors)
    tokens = serializer.save()
    return Response(tokens, status=status.HTTP_200_OK)


@extend_schema(
    request={'type': 'object', 'properties': {'refresh': {'type': 'string'}}},
    responses={204: None},
    tags=['auth'],
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    refresh = request.data.get('refresh')
    if not refresh:
        return Response({'detail': 'refresh es obligatorio'}, status=400)
    try:
        token = RefreshToken(refresh)
        token.blacklist()
    except TokenError:
        return Response({'detail': 'refresh inválido'}, status=400)
    return Response(status=204)


@extend_schema(responses=UserMeSerializer, tags=['users'])
@api_view(['GET'])
def me_view(request):
    serializer = UserMeSerializer(request.user)
    return Response(serializer.data)
