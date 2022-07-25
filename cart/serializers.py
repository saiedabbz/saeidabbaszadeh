from hq.utils import InsiderSerializer
from .models import Cart, CartItem

from product.serializers import MinimalProductVariantSerializer


class CartItemSerializer(InsiderSerializer):
    
    def _parser(self, instance: CartItem):
        return {
            'id': instance.id,
            'variant': MinimalProductVariantSerializer(instance.variant).data,
            'amount': instance.amount,
        }


class CartSerializer(InsiderSerializer):

    def _parser(self, instance: Cart):
        return {
            'id': instance.id,
            'items': CartItemSerializer(instance.items.all(), many=True).data,
        }
