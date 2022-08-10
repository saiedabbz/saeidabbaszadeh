from product.models import Collection, Product
from service.models import Service
from config.models import Config

from pprint import pprint

def load_configs():
    configs = Config.objects.all()
    g_configs = {}
    for config in configs:
        g_configs[config.slug] = config

    return g_configs



def render(request):
    categories = Collection.objects.filter(parent_id=None, collection_type_id=1)
    services = Service.objects.all()
    products = Product.objects.all()
    
    context = {
        'g_categories': categories ,
        'g_services': services ,
        'g_products': products ,
        'g_configs': load_configs()
    }

    return context