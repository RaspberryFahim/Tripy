from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import TripyUser


class UserAdminConfig(UserAdmin):
    model = TripyUser
    search_fields = ('email',)
    list_filter = ('email', 'is_staff')
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
    ordering = ('email',)
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'address', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'address', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )


admin.site.register(TripyUser, UserAdminConfig)
