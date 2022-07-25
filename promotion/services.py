from .models import Promotion
from .serializers import AllPromotionSerializer
import datetime
from django.db.models import Q

def load_promotions(now: datetime):
    promotions = Promotion.objects.filter(
        promotion_type__in = [Promotion.ON_COllECTION, Promotion.ON_PRODUCT],
        start_at__lt = now,
        end_at__gt = now
    )

    serialized = AllPromotionSerializer(promotions)
    return serialized.data


def promotion_by_product(product):
    now = datetime.datetime.now()
    return Promotion.objects.filter(
        Q(products=product) | Q(collections__in=product.collections.all())
    ).filter(
        start_at__lt=now,
        end_at__gt=now,
        active=True
    ).distinct().order_by('-created_at').first()


def promotion_by_collection(collection):
    now = datetime.datetime.now()
    return Promotion.objects.filter(
        collections=collection,
        start_at__lt=now,
        end_at__gt=now,
        active=True
    ).distinct().order_by('-created_at').first()


def get_discount(variant, promotion=None, check=True):

    if check:
        now = datetime.datetime.now()
        promotion = Promotion.objects.filter(
            Q(products=variant.product) | Q(collections__in=variant.product.collections.all())
        ).filter(
            start_at__lt=now,
            end_at__gt=now,
            active=True
        ).distinct().order_by('-created_at').first()


    price = variant.price
    discount = 0
    discount_type = "NONE"

    if promotion is not None:
        discount = promotion.discount
        discount_type = promotion.discount_type
        price -= (price * discount) // 100 if discount_type == Promotion.PERCENT else discount
        # price -= ds

    return {
        "base_price": variant.price,
        "discount": discount,
        "discount_type": discount_type,
        "price": price
    }