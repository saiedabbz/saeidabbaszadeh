from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from default.models import Category
from product.models import Product
from order.models import Order
from customer.models import Customer
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,logout

from django.views.generic import UpdateView
from django.template import loader


def HomePage(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html' , {'categories': categories, 'products': products })



def ProductsView(request, cat_id):
    products = Product.objects.filter(category_id=cat_id)

    category = Category.objects.get(pk=cat_id)

    return render(request, category.theme , {'products': products})


def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        customer = User.objects.create_user(username,email,pass1)
        customer.first_name = first_name
        customer.last_name = last_name
        customer.save()
        return redirect('login')

    return render(request,'register.html')


def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('homepage')
        else:
            return redirect('login')
    return render(request,'login.html')







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
        category = Category(title=cat_title, theme=cat_theme)
        category.save()
        return redirect('category_list')
    return render(request, 'add_category.html', )


def EditCategory(request, id):
    category = Category.objects.get(pk=id)
    return render(request, 'edit_category.html',{'category': category })


def UpdateCategory(request, id):

    category_title = request.POST['title']
    
    category = Category.objects.get(pk=id)
    category.title = category_title
    category.save()

    return redirect('category_list')