from django.urls import path

from . import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('core/organos/', views.OrganoListView.as_view(), name='organos-list'),
    path('core/tipos-juicio/', views.TipoJuicioListView.as_view(), name='tipos-juicio-list'),
]
