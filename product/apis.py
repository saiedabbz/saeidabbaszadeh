import datetime
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from hq.io import response

from product.services import collections, product_detail, products
from promotion.services import load_promotions

def eset_list(request):
	context = {
			'products': 'ssss',
            'page_title': 'لیست محصولات امنیت سایبری ESET',
			}
	return render(request, 'it_theme/product/eset_list.html', context)

def eset_detail(request):
	context = {
			'product': 'ssss',
            'page_title': 'ESET INTERNET SECURITY',
			}
	return render(request, 'it_theme/product/eset_detail.html', context)

def kaspersky_list(request):
	context = {
			'products': 'ssss',
            'page_title': 'لیست محصولات امنیت سایبری Kaspersky',
			}
	return render(request, 'it_theme/product/kaspersky_list.html', context)

def kaspersky_detail(request):
	context = {
			'product': 'ssss',
            'page_title': 'Kaspersky Anti-Virus',
			}
	return render(request, 'it_theme/product/kaspersky_detail.html', context)


@csrf_exempt
@api_view(['GET'])
def home_page(request):
    return response({
        "showcase": products({'showcase': True, "page_limit": 4})['items'],
        "sales": products({"page_limit": 4, "on_sale": True})['items'],
        "recommendations": products({"page_limit": 10})['items'],
        "collections": collections({"collection_type": "MAIN", "parent": 0})
    })



@csrf_exempt
@api_view(['GET'])
def load_collections(request):
    parent_id = request.GET.get("parent", None)
    if parent_id is not None:
        return response({"collections": collections({**request.query_params}), 
                        "collection": collections({"id": parent_id}), 
                        "products": products({"collection": [parent_id]}), "collection_parent":parent_id})
    else:
        return response({"collections": collections({**request.query_params})})


@csrf_exempt
@api_view(['GET'])
def load_products(request):
    return response({"products": products({**request.query_params}),
                     "collections": collections({"parent": request.GET.get('collection')}),
                     "collection": collections({"id": request.GET.get('collection')})})


@csrf_exempt
@api_view(['GET'])
def load_product_detail(request, product_slug):
    return response({"product": product_detail(product_slug)})
