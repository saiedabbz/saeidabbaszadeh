from django.contrib import admin

from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'company_name',
        'first_name',
        'last_name',
        'email',
        'phone',
        'quantity',
        'slug',
        'product',
        'description',
        'created_at',
        'contact_type',
        
    ]