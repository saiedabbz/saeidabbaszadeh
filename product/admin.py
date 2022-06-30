from django.contrib import admin
from product.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category','name','image')


admin.site.register(Product,ProductAdmin)
