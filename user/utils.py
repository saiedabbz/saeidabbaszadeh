from hq.utils import QueryBuilder


class UserQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        super().__init__(kwargs)

    def _resolve_id(self, value):
        self._query['id'] = value


class AddressQueryBuilder(QueryBuilder):
    def __init__(self, kwargs: dict):
        if 'active' not in kwargs:
            kwargs['active'] = True

        super().__init__(kwargs)

    def _resolve_id(self, value):
        self._query['id'] = value

    def _resolve_user_id(self, value):
        self._query['user_id'] = value

    def _resolve_user(self, value):
        self._query['user'] = value
