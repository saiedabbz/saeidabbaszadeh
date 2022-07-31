from product.models import Collection, Product
from service.models import Service

def render(request):
    categories = Collection.objects.filter(parent_id=None, collection_type_id=1)
    services = Service.objects.all()
    products = Product.objects.all()
    
    context = {
        'g_categories': categories ,
        'g_services': services ,
        'g_products': products ,
    }

    return context