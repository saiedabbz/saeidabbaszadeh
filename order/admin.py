from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cart_id',
        'state',
        'username',
        'address_id',
        'transaction_id',
        'created_at',
    ]

    def username(self, obj):
        return obj.user.username


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order_id',
        'username',
        'variant_id',
        'variant_title',
        'price',
        'created_at',
    ]

    def username(self, obj):
        return obj.order.user.username

    def variant_title(self, obj):
        return obj.variant.product.title