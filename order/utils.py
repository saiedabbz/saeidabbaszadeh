from hq.utils import QueryBuilder


class OrderQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        super().__init__(kwargs)

    def _resolve_id(self, value):
        self._query['id'] = value

    def _resolve_cart(self, value):
        self._query['cart'] = value

    def _resolve_cart_id(self, value):
        self._query['cart_id'] = value

    def _resolve_user_id(self, value):
        self._query['user_id'] = value

    def _resolve_user(self, value):
        self._query['user'] = value

    def _resolve_state(self, value):
        self._query['state'] = value


class OrderItemQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        super().__init__(kwargs)

    def _resolve_id(self, value):
        self._query['id'] = value

    def _resolve_order_id(self, value):
        self._query['order_id'] = value

    def _resolve_order(self, value):
        self._query['order'] = value