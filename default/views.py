from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from default.models import Category
from product.models import Product
from order.models import Order
from customer.models import Customer
# from django.contrib.auth.models import User
from django.shortcuts import redirect
# from django.contrib.auth import authenticate, login,logout

from django.views.generic import UpdateView
from django.template import loader


def Navbar(request, id):

    products = Product.objects.filter(category_id=id)
    category = Category.objects.all()

    return render(request, 'nav.html', {'products': products, 'category': category })




def HomePage(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html' , {'categories': categories, 'products': products })



def ProductsView(request, cat_id):
    products = Product.objects.filter(category_id=cat_id)

    category = Category.objects.get(pk=cat_id)

    return render(request, category.theme , {'products': products})






def Categories(request):
    category = Category.objects.all()

    return render(request, 'category_list.html',{'category': category })


def Delete(request, id):
    category = Category.objects.get(pk=id)
    category.delete()
    return redirect('category_list')


def AddCategory(request):
    if request.method == "POST":
        cat_title = request.POST.get('title')
        cat_theme = request.POST.get('theme')
        image = request.FILES.get('cat_image')

        category = Category(title=cat_title, theme=cat_theme, cat_image=image)
        category.save()
        return redirect('category_list')
    return render(request, 'add_category.html', )


def EditCategory(request, id):
    category = Category.objects.get(pk=id)
    return render(request, 'edit_category.html',{'category': category })


def UpdateCategory(request, id):

    title = request.POST.get('title')
    cat_image = request.FILES.get('cat_image')
    
    category = Category.objects.get(pk=id)

    category.title = title

    if cat_image:
        category.cat_image = cat_image

    category.save()

    return redirect('category_list')





def EsetNod(request):
    return render(request, 'eset_detail/eset_detail_nod.html')

def EsetInternet(request):
    return render(request, 'eset_detail/eset_detail_internet.html')

def EsetSmart(request):
    return render(request, 'eset_detail/eset_detail_smart.html')