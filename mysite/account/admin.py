from django.contrib import admin

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import SimpleListFilter


class CustomUserAdmin(UserAdmin):
    search_fields = ('email', 'username')
    list_display = ('email', 'username', 'email', 'is_staff', 'is_active', 'is_api')
    list_filter = ('email', 'is_staff', 'is_active',)
    filter_horizontal = ('groups', 'user_permissions',)

    class Meta:
        model = CustomUser
    
admin.site.register(CustomUser, CustomUserAdmin)
