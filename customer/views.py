from django.shortcuts import render, redirect

from default.models import Category
from order.models import Order
from customer.models import Customer




def CustomerList(request):
    customers = Customer.objects.all()
    return render(request,'customers.html',{'customers': customers})

def AddCustomer(request):
    if request.method == "POST":
        customer_name = request.POST.get('customer')
        ctm = Customer(name=customer_name)
        ctm.save()
        return redirect('customerlist')

    return render(request,'add_customer.html')

def DeleteCustomer(request, id):
    ctm = Customer.objects.get(pk=id)
    ctm.delete()
    return redirect('customerlist')


def UpdateCustomer(request ,id):
    ctm = Customer.objects.get(pk=id)
    return render(request, 'updatecustomer.html',{'ctm': ctm})


def UpdateCustomerRecord(request, id):
    customer_name = request.POST['name']
    ctm = Customer.objects.get(pk=id)
    ctm.name = customer_name
    ctm.save()
    return redirect('customerlist')