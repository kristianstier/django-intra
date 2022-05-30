from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Announcement

class IntraUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'department', 'jobtitle', 'is_staff',
        )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('department', 'jobtitle', 'telefon', 'age', 'image_tag', 'image')
        })
    )
    readonly_fields = ['image_tag']

admin.site.register(User, IntraUserAdmin)
admin.site.register(Announcement)