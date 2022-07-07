from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from default.models import Category
from product.models import Product



def HomePage(request):
    categories = Category.objects.all()
    return render(request, 'index.html' , {'categories': categories})



def ProductsView(request, cat_id):
    products = Product.objects.filter(category_id=cat_id)

    category = Category.objects.get(pk=cat_id)

    return render(request, category.theme , {'products': products})

