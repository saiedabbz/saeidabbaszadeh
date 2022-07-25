from pprint import pprint
from rest_framework import serializers
from hq.utils import InsiderSerializer
from .models import (
    Product, ProductOption, Collection, ProductVariant
)

from promotion.services import get_discount, promotion_by_product



class ProductOptionSerializer(InsiderSerializer):
    def __init__(self, instance, **kwargs):
        super().__init__(instance, **kwargs)

    def _parser(self, instance: ProductOption):
        return {
            "field":instance.group.field,
            "value": instance.value
        }


class MinimalProductVariantSerializer(InsiderSerializer):
    def __init__(self, instance, showcase: bool = False, promotion = None, check_promotion= True, **kwargs):
        self._promotion = promotion
        self._is_showcase = showcase
        self._check_promotion = check_promotion
        super().__init__(instance, **kwargs)

    
    def _parser(self, instance):
        return {
            'variant_id': instance.id,
            'product_id': instance.product.id,
            'title': instance.product.title,
            "slug": instance.product.slug,
            'description': instance.product.description,
            'price': self._price(instance),
            'options': ProductOptionSerializer(instance.options.all(), many=True).data,
            'image': self._image(instance)
        }

    def _image(self, variant: ProductVariant):
        if self._is_showcase:
            if variant.product.showcases.exists():
                return variant.product.showcases.all().order_by('-created_at')[0].image.url
            
        else:
            if variant.product.images.exists():
                return variant.product.images.all().order_by('created_at')[0].image.url

        return ""

    def _price(self, variant: ProductVariant):
        return get_discount(variant, self._promotion, self._check_promotion)


class MiniCollectionSerializer(serializers.ModelSerializer):
    type_title = serializers.CharField(source='collection_type.title')

    class Meta:
        model = Collection
        fields = [
            "id",
            "type_title",
            "slug",
            "title",
            "image",
        ]


class ProductSerializer(InsiderSerializer):
    def __init__(self, instance, **kwargs):
        super().__init__(instance, **kwargs)

    def _parser(self, instance: Product):
        promotion = self._promotion_parser(instance)

        return {
            "title": instance.title,
            "description": instance.description,
            "slug": instance.slug,
            "collections": CollectionSerializer(instance.collections.all(), many=True).data,
            "images": self._image_parser(instance),
            # "promotions": promotion,
            "variants": MinimalProductVariantSerializer(instance.variants.all(), promotion=promotion, check_promotion=False, many=True).data,
        }

    def _image_parser(self, instance: Product):
        # return instance.images.all().values_list('image', flat=True)
        return [image.image.url for image in instance.images.all()]


    def _promotion_parser(self, instance: Product):
        return promotion_by_product(instance)


class CollectionSerializer(serializers.ModelSerializer):
    type_title = serializers.CharField(source='collection_type.title')
    childs = MiniCollectionSerializer(source='collection_set', many=True, read_only=True)
        
    class Meta:
        model = Collection
        fields = [
            "id",
            "type_title",
            "slug",
            "title",
            "image",
            "childs"
        ]