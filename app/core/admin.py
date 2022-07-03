from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import User
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email']
    readonly_fields = ('last_login',)
    fieldsets = (
        (None,{
            'fields':('email','password','name'),
            'classes':('wide','extrapretty')
        }),
        ('Permissions',{
            'fields':('is_staff','is_active','is_superuser')
        }),
        (
            'Important Dates',{
                'fields':('last_login',)
            }
        ),(
            'Groups',{
                'fields':('user_permissions','groups')
            }
        )
    )

    add_fieldsets = (
        (None,{
            'fields':('email','password','name'),
            'classes':('wide','extrapretty')
        }),
        ('Permissions',{
            'fields':('is_staff','is_active','is_superuser')
        }),

    )


admin.site.register(User,UserAdmin)

