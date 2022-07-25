from django.http import Http404
from django.db.models import Q

from hq.utils import page_builder
from .models import Product, Collection, ProductImage, ProductVariant, Showcase
from .serializers import CollectionSerializer, MinimalProductVariantSerializer, ProductSerializer
from .utils import CollectionQueryBuilder, ProductQueryBuilder, ProductVariantQueryBuilder

from promotion.models import Promotion
from pprint import pprint

def collections(filters: dict) -> list:
    build = CollectionQueryBuilder(filters)
    data = Collection.objects.filter(**build.query).order_by(build.sort_by)
    serialized = CollectionSerializer(data, many=True)
    return serialized.data


def products(filters: dict):
    build = ProductVariantQueryBuilder(filters)
    data = ProductVariant.objects.filter(**build.query)
    if build.on_sale:
        data = data.filter(build.sale_query())

    data = data.order_by(build.sort_by)
    return page_builder(data, MinimalProductVariantSerializer, build.page_data)


def product_detail(product_slug: str) -> dict:
    build = ProductQueryBuilder({"slug": product_slug})
    if not Product.objects.filter(**build.query).exists():
        raise Http404

    product = Product.objects.get(**build.query)
    serialized = ProductSerializer(product)
    return serialized.data


def get_variant(variant_id: int):
    build = ProductVariantQueryBuilder({"id": variant_id})
    if not ProductVariant.objects.filter(**build.query).exists():
        raise Http404

    return ProductVariant.objects.get(**build.query)