from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from user.models import User, UserAddress

class ZillooUserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'username',]

admin.site.register(User, ZillooUserAdmin)


@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'username',
        'state',
        'city',
        'full_name',
        'mobile',
        'active',
        'created_at',
    ]

    def username(self, obj):
        return obj.user.username
