from .models import Order, OrderItem
from hq.utils import InsiderSerializer

from user.serializers import UserAddressOneSerializer
from product.serializers import MinimalProductVariantSerializer


class OrderItemSerializer(InsiderSerializer):

    def _parser(self, instance: OrderItem):
        return {
            "id": instance.id,
            "variant": MinimalProductVariantSerializer(instance.variant).data,
            "price": instance.price,
            "promotion": self._promotion_parser(instance.promotion)
        }

    def _promotion_parser(self, promotion):
        discount = 0
        discount_type = "NONE"
        if promotion is not None:
            discount = promotion.discount
            discount_type = promotion.discount_type

        return {
            "discount": discount,
            "discount_type": discount_type
        }


class OrderSerializer(InsiderSerializer):

    def _parser(self, instance: Order):
        return {
            "id": instance.id,
            "items": OrderItemSerializer(instance.items.all(), many=True).data,
            "state": instance.state,
            "address": UserAddressOneSerializer(instance.address).data if instance.address is not None else None,
            "date": instance.date,
            "time": instance.time, 
            "transaction": None, # TODO: change to serializer after adding bank
            "created_at": instance.created_at.strftime("%Y-%m-%d")
        }
