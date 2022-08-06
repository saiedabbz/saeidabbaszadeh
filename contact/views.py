# from contextlib import redirect_stderr
# from itertools import product
from django.shortcuts import render, redirect
from contact.models import Contact
from product.models import Product


def InQuery(request, slug):
    products = Product.objects.all()

    if request.method == "POST":
        product = request.POST.get('product')
        company_name = request.POST.get('company_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')

        prod = Product.objects.get(pk=product)

        contact = Contact(product=prod, company_name=company_name, first_name=first_name, last_name=last_name, email=email, phone=phone, quantity=quantity, description=description )
        contact.save()
        return redirect("homepage")

    return render(request, 'add_inquery.html', {'products': products,})