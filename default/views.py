from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from default.models import Category
from product.models import Product



def HomePage(request):
    categories = Category.objects.all()
    context ={
        'categories': categories,
    }
    return render(request, 'index.html' , context)


def EssetView(request):
    products = Product.objects.all()
    context ={
        'products': products
    }
    return render(request, 'esset.html', context)




def Node32View(request):
    return render(request,'node32.html')