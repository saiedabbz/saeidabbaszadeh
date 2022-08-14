from django.shortcuts import render, redirect
from contact.models import Contact
from product.models import Product
from service.models import Service

def addInquery(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        product = ""

    try:
        service = Service.objects.get(slug=slug)
    except: 
        service = ""


    print(f"product: {product} , service: {service}")

    return render(request, 'add_inquery.html', {'product': product, 'service': service})





def insertInquery(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except:
        product = 0

    try:
        service = Service.objects.get(slug=slug)
    except: 
        service = 0

    if request.method == "POST":
        company_name = request.POST.get('company_name')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        quantity = request.POST.get('quantity')
        description = request.POST.get('description')
        # inquery_type = request.POST.get('inq_type')

        contact = Contact()
        
        if product != 0 :
            contact.product = product
        else:
            contact.service = service
        contact.company_name = company_name
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.quantity = quantity
        contact.description = description
        # contact.inquery_type = int(inq_type)

        contact.save()
        return redirect("homepage")

    