from importlib.resources import contents
from multiprocessing import context
from django.shortcuts import render, redirect
from contact.models import Contact, InQueryType
from product.models import Product
from service.models import Service

def success(request):
    contact = Contact.objects.all()
    inq_type = InQueryType.objects.all()

    context = {
        'contact': contact ,
        'inq_type': inq_type ,
    }
    return render(request, 'success.html', context)

def addContactUs(request):
    return render(request, 'contact_us.html')



def insertContactUs(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        contact = Contact()

        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.inquery_type_id = 3
        contact.description = description

        contact.save()

    return redirect("success")






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
            contact.inquery_type_id = 1
        else:
            contact.service = service
            contact.inquery_type_id = 2
        contact.company_name = company_name
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.quantity = quantity
        contact.description = description
        # contact.inquery_type = int(inq_type)

        contact.save()
        return redirect("success")

    