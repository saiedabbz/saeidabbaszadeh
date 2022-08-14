from django.contrib import admin

from .models import Contact , InQueryType


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'product',
        'service',
        'company_name',
        'name',
        'email',
        'phone',
        'quantity',
        # 'slug',
        # 'description',
        'created_at',
        # 'inquery_type',
        
    ]

@admin.register(InQueryType)
class InQueryTypeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'active',
    
    ]