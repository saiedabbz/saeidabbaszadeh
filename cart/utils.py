from hq.utils import QueryBuilder


class CartQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        if 'active' not in kwargs:
            kwargs['active'] = True

        super().__init__(kwargs)

    def _resolve_user(self, value):
        self._query['user'] = value


class CartItemQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        if 'active' not in kwargs:
            kwargs['active'] = True

        super().__init__(kwargs)

    def _resolve_cart(self, value):
        self._query['cart'] = value

    def _resolve_variant(self, value):
        self._query['variant'] = value

    def _resolve_variant_id(self, value):
        self._query['variant_id'] = value