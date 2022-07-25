from django.core.paginator import Paginator
from django.db.models import QuerySet
import datetime



class QueryBuilder:
    def __init__(self, kwargs: dict):
        self._query = {}
        self._sort = "-created_at"
        self._pagination = {
            "page": 1,
            "limit": 20,
        }

        for k, v in kwargs.items():
            if v is None or not hasattr(self, f'_resolve_{k}'):
                continue

            getattr(self, f'_resolve_{k}')(v) 


    def _resolve_page(self, value):
        value = value[0] if isinstance(value, list) else value
        self._pagination["page"] = int(value) if isinstance(value, str) else value

    
    def _resolve_page_limit(self, value):
        self._pagination["limit"] = int(value) if isinstance(value, str) else value


    def _resolve_from_date(self, value):
        self._query['created_at__gt'] = value


    def _resolve_active(self, value):
        self._query['active'] = value


    def _resolve_to_date(self, value):
        to_date = datetime.datetime.strptime(value, "%Y-%m-%d")
        to_date = to_date + datetime.timedelta(days=1)
        to_date = to_date.strftime("%Y-%m-%d")
        self._query['created_at__lt'] = to_date

    
    def _resolve_sort(self, value):
        order_keys = {
            'date_asc': 'created_at',
            'date_desc': '-created_at',
            'title_asc': 'title',
            'title_desc': '-title',
        }

        self._sort = order_keys.get(value, '-created_at')


    @property
    def query(self):
        return self._query

    
    @property
    def sort_by(self):
        return self._sort

    
    @property
    def page_data(self):
        return self._pagination



def page_builder(query_set: QuerySet, serializer, page_data: dict):
    
    paged = Paginator(query_set, page_data["limit"])
    current = paged.page(page_data["page"])
    serialized = serializer(current.object_list, many=True)

    return {
        "items": serialized.data,
        "pages": {
            "page": page_data["page"],
            "page_limit": page_data["limit"],
            "total_pages": paged.num_pages
        }
    }



class InsiderSerializer:
    def __init__(self, instance, **kwargs):
        self._instance = instance
        
        if kwargs.get('many', False):
            self._data = [self._parser(item) for item in instance]
        else:
            self._data = self._parser(instance)


    def _parser(self, instance):
        raise NotImplementedError('`to_representation()` must be implemented.')


    @property
    def data(self):
        return self._data






