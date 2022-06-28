from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from default.models import Category
# Create your views here.

def HomePage(request):
    obj = Category.objects.get(id=1)
    context ={
        'title': obj.title,
    }
    return render(request, 'index.html' , context)


def EssetView(request):
    return render(request, 'esset.html')