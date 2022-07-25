import datetime
from hq.utils import QueryBuilder
from django.db.models import Q



class ProductQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        if 'active' not in kwargs:
            kwargs['active'] = True

        super().__init__(kwargs)

    def _resolve_collection(self, value):
        self._query['collections__in'] = value if isinstance(value, list) else [value]


    def _resolve_title(self, value):
        self._query['title__icontains'] = value


    def _resolve_slug(self, value):
        self._query['slug'] = value


class ProductVariantQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        if 'active' not in kwargs:
            kwargs['active'] = True

        if 'has_stock' not in kwargs:
            kwargs['has_stock'] = True

        if 'main' not in kwargs:
            kwargs['main'] = True

        self._on_sale = False
        super().__init__(kwargs)
        

    def _resolve_id(self, value):
        self._query['id'] = value

    def _resolve_collection(self, value):
        self._query['product__collections__in'] = value if isinstance(value, list) else [value]

    def _resolve_collection_slug(self, value):
        self._query['product__collections__slug__in'] = value if isinstance(value, list) else [value]


    def _resolve_title(self, value):
        self._query['product__title__icontains'] = value


    def _resolve_slug(self, value):
        self._query['product__slug'] = value


    def _resolve_main(self, value):
        self._query['is_main'] = value


    def _resolve_has_stock(self, value):
        if value:
            self._query['stock__gt'] = 0
        else:
            self._query['stock'] = 0


    def _resolve_options(self, value):
        self._query['options__in'] = value if isinstance(value, list) else [value]

    
    def _resolve_showcase(self, value):
        self._query['product__showcases__isnull'] = False
        self._query['product__showcases__active'] = True
        self._sort = '-product__showcases__created_at'


    def _resolve_on_sale(self, value):
        value = value[0] if isinstance(value, list) else value
        if isinstance(value, str):
            value = True if value == 'true' else False
        self._on_sale = value

    @property
    def on_sale(self):
        
        return self._on_sale


    def sale_query(self):
        now = datetime.datetime.now()
        return Q(
            product__collections__promotions__isnull=False,
            product__collections__promotions__active=True,
            product__collections__promotions__start_at__lt=now,
            product__collections__promotions__end_at__gt=now
        ) | Q(
            product__promotions__isnull=False,
            product__promotions__active=True,
            product__promotions__start_at__lt=now,
            product__promotions__end_at__gt=now
        )



class CollectionQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        if 'active' not in kwargs:
            kwargs['active'] = True

        if 'is_private' not in kwargs:
            kwargs['is_private'] = False

        super().__init__(kwargs)

    def _resolve_parent(self, value):
        if value == 0:
            self._query['parent_id'] = None
        else:
            self._query['parent_id__in'] = value


    def _resolve_title(self, value):
        self._query['title__icontains'] = value

    def _resolve_id(self, value):
        self._query['id'] = value

    def _resolve_slug(self, value):
        self._query['slug'] = value


    def _resolve_is_private(self, value):
        self._query['is_private'] = value


    def _resolve_collection_type(self, value):
        self._query['collection_type__title__in'] = value if isinstance(value, list) else [value]
