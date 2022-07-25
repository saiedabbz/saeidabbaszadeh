from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'active',
        'created_at',
    ]

    def username(self, obj):
        return obj.user.username


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cart_id',
        'username',
        'variant_id',
        'variant_title',
        'amount',
        'active',
        'created_at',
    ]

    def username(self, obj):
        return obj.cart.user.username

    def variant_title(self, obj):
        return obj.variant.product.title