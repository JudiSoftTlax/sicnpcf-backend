from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'rol', 'organo', 'mfa_enabled', 'is_active')
    list_filter = ('rol', 'organo', 'mfa_enabled', 'is_active')
    search_fields = ('email', 'curp', 'first_name', 'last_name')
    ordering = ('email',)
    fieldsets = UserAdmin.fieldsets + (  # type: ignore[operator]
        ('SICNPCF', {'fields': ('curp', 'organo', 'rol', 'institution_id',
                                'mfa_enabled', 'last_login_ip')}),
    )
