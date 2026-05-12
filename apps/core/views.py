"""Core views: health + catalog listings."""
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from rest_framework import filters, generics
from rest_framework.permissions import AllowAny

from apps.core.models import Organo, TipoJuicio
from apps.core.serializers import OrganoSerializer, TipoJuicioSerializer


@require_GET
def health(request):
    return JsonResponse({'status': 'ok', 'version': '0.1.0'})


class OrganoListView(generics.ListAPIView):
    serializer_class = OrganoSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['clave', 'nombre', 'distrito']

    def get_queryset(self):
        qs = Organo.objects.all()
        materia = self.request.query_params.get('materia')
        if materia:
            qs = qs.filter(materia=materia)
        return qs


class TipoJuicioListView(generics.ListAPIView):
    serializer_class = TipoJuicioSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = TipoJuicio.objects.all()
        materia = self.request.query_params.get('materia')
        if materia:
            qs = qs.filter(materia=materia)
        return qs
