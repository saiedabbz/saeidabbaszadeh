from .utils import CartQueryBuilder, CartItemQueryBuilder
from .serializers import CartItemSerializer, CartSerializer
from .models import Cart, CartItem

from user.models import User
from product.services import get_variant

def load_active_cart(user: User):
    build = CartQueryBuilder({"user": user})
    cart = Cart.objects.filter(**build.query).order_by(build.sort_by).first()
    if cart is None:
        cart = Cart.objects.create(user=user)

    return cart


def load_cart(user: User):
    cart = load_active_cart(user)
    return CartSerializer(cart).data


def cart_item_amount(user: User, variant_id: int, amount: int = 1):
    cart = load_active_cart(user)
    variant = get_variant(variant_id)
    build = CartItemQueryBuilder({"cart": cart, "variant": variant})

    if not CartItem.objects.filter(**build.query).exists() and amount > 0:
        item = CartItem.objects.create(
            cart=cart,
            variant_id=variant_id,
            amount=amount
        )
        
    else:
        item = CartItem.objects.get(**build.query)
        if amount > 0:
            item.amount = amount
            item.save()
        else:
            item.delete()

    return amount



def append_cart_items(user: User, items: list):
    cart = load_active_cart(user)
    cart_items = [CartItem(cart=cart, variant_id=i['variant_id'], amount=i['amount']) for i in items]
    CartItem.objects.bulk_create(cart_items)
    return CartSerializer(cart).data
