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
    return render(request, 'index.html' , {'categories': categories})



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


def Logout(reqeust):
    logout(reqeust)
    return render(request,'index.html')





def OrderView(request):
    order = Order.objects.all()
    return render(request,'order.html',{'order': order})


def AddOrder(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    if request.method == "POST":
        customer = request.POST.get('customer')
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')

        print("*****", customer)
        c = Customer.objects.get(pk=customer)
        p = Product.objects.get(pk=product)
        order = Order(customer=c, product=p, quantity=quantity)
        # order.customer = customer
        # order.product = product
        # order.quantity = quantity
        order.save()
        return redirect('order')


    return render(request,'addorder.html',{'customers': customers,
        'products': products})


def DeleteOrder(request, id):
    order = Order.objects.get(id=id)
    order.delete()
    return redirect('order')


def UpdateOrder(request, id):
    customers = Customer.objects.all()
    products = Product.objects.all()
    order = Order.objects.get(id=id)
    context ={
        
        'order': order

    }
    return render(request, 'update.html', context)


def UpdateRecords(request, id):

    # customer = request.POST['customer']
    # product = request.POST['product']
    quantity = request.POST['quantity']

    # c = Customer.objects.get(pk=customer)
    # p = Product.objects.get(pk=product)

    order = Order.objects.get(id=id)
    # order.customer = c 
    # order.product = p
    order.quantity = quantity 

    order.save()
    return redirect('order')
