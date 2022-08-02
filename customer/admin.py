from asyncio import format_helpers
from django.contrib import admin
from . models import Customer


# admin.site.register(Customer,)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'image',
        'date_joined',
        'active',
    ]


    def image(self, obj):
        if obj.image != '':
            return format_helpers('<img src="{}" style="width: 100px; height: 100px;" />'.format(obj.image.url))
        return ''

    def title(self, obj):
        return obj.title