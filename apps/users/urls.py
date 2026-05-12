from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users import views

urlpatterns = [
    path('auth/login', views.login_view, name='auth-login'),
    path('auth/refresh', TokenRefreshView.as_view(), name='auth-refresh'),
    path('auth/logout', views.logout_view, name='auth-logout'),
    path('users/me', views.me_view, name='users-me'),
]
