from django.db.models import QuerySet
from .models import Promotion



class AllPromotionSerializer:
    def __init__(self, query_set: QuerySet):
        self._data = query_set
        self._result = {
            "collections": [],
            "products": []
        }

    def _on_collection(self, promotion: Promotion):
        self._result['collections'].append({
            "promotion": promotion,
            "ids": promotion.collections.all().values_list('id', flat=True)
        })
        

    def _on_product(self, promotion: Promotion):
        self._result['products'].append({
            "promotion": promotion,
            "ids": promotion.products.all().values_list('id', flat=True)
        })


    @property
    def data(self):
        for promotion in self._data:
            getattr(self, f'_{promotion.promotion_type.lower()}')(promotion)
        return self._result