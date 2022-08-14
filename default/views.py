# from gc import get_objects
# from itertools import product
# from multiprocessing import context
# from unicodedata import category
from http.client import REQUEST_URI_TOO_LONG
from urllib import request
from django.shortcuts import render
from default.models import Category
from product.models import Product, Collection, ProductImage
from django.shortcuts import redirect
from service.models import Service
from customer.models import Customer
from config.models import Config

from django.views.generic import UpdateView
from django.template import loader

from product.services import collections, product_detail, products

from pprint import pprint




def HomePage(request):
    categories = Collection.objects.filter(parent_id=None, collection_type_id=1)
    services = Service.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()
    top_products_business = Product.objects.filter(collections__collection_type_id=4).order_by("order_id")[:3]
    top_products_home = Product.objects.filter(collections__collection_type_id=3).order_by("order_id")[:3]
    
    context = {
        'categories': categories ,
        'services': services ,
        'products': products ,
        'customers': customers ,
        'top_products': {
            'business': top_products_business,
            'home': top_products_home
        }
    }
    
    return render(request, 'index.html', context)



def ProductsView(request, slug):
    products = Product.objects.filter(collections__slug=slug)
    # prod = products.objects.all()
    context = {
        'products': products ,
        # 'prod': prod
    }
    return render(request, products[0].collections.first().theme , context )







def Categories(request):
    category = Category.objects.all()
    return render(request, 'category/category_list.html',{'category': category })


def Delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('category/category_list')


def AddCategory(request):
    if request.method == "POST":
        cat_title = request.POST.get('title')
        cat_theme = request.POST.get('theme')
        image = request.FILES.get('cat_image')
        category = Category(title=cat_title, theme=cat_theme, cat_image=image)
        category.save()
        return redirect('category_list')
    return render(request, 'category/add_category.html', )


def EditCategory(request, id):
    category = Category.objects.get(pk=id)
    return render(request, 'category/edit_category.html',{'category': category })


def UpdateCategory(request, id):
    title = request.POST.get('title')
    cat_image = request.FILES.get('cat_image')
    category = Category.objects.get(pk=id)
    category.title = title
    if cat_image:
        category.cat_image = cat_image
    category.save()
    return redirect('category/category_list')





def ProductDetail(request, pro_slug):
    product = Product.objects.get(slug=pro_slug)
    theme  = 'slide/product/' + product.collections.all()[0].theme

    print(theme)
    
    context = {
            'product': product,
            }
    return render(request, theme, context)



def ServiceView(request, slug):
    service = Service.objects.get(slug=slug)
    context = {
        'service': service ,
    }
    return render(request, 'services.html', context )

