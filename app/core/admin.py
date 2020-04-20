from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Tag, Ingredient, Recipe
from django.utils.translation import gettext as _


class UserAdmin(BaseUserAdmin):
    # choose the list ordering by id
    ordering = ['id']
    # choose attributes columns of the list
    list_display = ['email', 'name']
    # choose fields of each detail
    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    # choose fields required when creating new user object
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name')
        }),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe)
