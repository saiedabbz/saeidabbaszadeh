from django.http import Http404
from user.models import User
from cart.models import Cart
from cart.services import load_active_cart

from .models import Order, OrderItem
from .serializers import OrderItemSerializer, OrderSerializer
from .utils import OrderQueryBuilder, OrderItemQueryBuilder

from hq.utils import page_builder


def get_one_order(user: User, order_id: int):
    build = OrderQueryBuilder({"user": user, "id": order_id})
    if not Order.objects.filter(**build.query).exists():
        raise Http404

    return Order.objects.get(**build.query)


def init_order(user: User):
    cart = load_active_cart(user)
    order = Order.objects.create(
        cart = cart,
        user = user
    )

    return OrderSerializer(order).data


def order_address(user: User, order_id: int, data: dict):
    order = get_one_order(user, order_id)
    order.address_id = data['address_id']
    order.save()
    return OrderSerializer(order).data


def order_datetime(user: User, order_id: int, data: dict):
    order = get_one_order(user, order_id)
    order.date = data['date']
    order.time = data['time']
    order.save()
    return OrderSerializer(order).data


def payment(user: User, order_id: int):
    order = get_one_order(user, order_id)
    return OrderSerializer(order).data


def load_order(user: User, order_id: int):
    order = get_one_order(user, order_id)
    return OrderSerializer(order).data


def load_orders(user: User, filters: dict):
    build = OrderQueryBuilder({"user": user, **filters})
    orders = Order.objects.filter(**build.query).order_by(build.sort_by)
    return page_builder(orders, OrderSerializer, build.page_data)
