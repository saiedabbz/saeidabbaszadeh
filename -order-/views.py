from django.shortcuts import render
from django.shortcuts import redirect


from order.models import Order
from default.models import Category
from product.models import Product
from customer.models import Customer



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
        'customers': customers,
        'products': products,
        'order': order,
    }
    return render(request, 'update.html', context)


def UpdateRecords(request, id):

    customer = request.POST['customer']
    product = request.POST['product']
    quantity = request.POST['quantity']

    c = Customer.objects.get(pk=customer)
    p = Product.objects.get(pk=product)

    order = Order.objects.get(id=id)
    order.customer = c 
    order.product = p
    order.quantity = quantity 

    order.save()
    return redirect('order')