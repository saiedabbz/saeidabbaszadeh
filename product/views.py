from unicodedata import category
from django.shortcuts import render
from django.shortcuts import redirect

from default.models import Category
from product.models import Product


def ProductList(request):
    products = Product.objects.all()

    return render(request, 'product_list.html',{'products': products })


def DeleteProduct(request, id):
    products = Product.objects.get(pk=id)
    products.delete()
    return redirect('productlist')



def AddProduct(request):
    categories = Category.objects.all()

    if request.method == "POST":
        category = request.POST.get('category')
        name = request.POST.get('name')
        image = request.FILES.get('image')

        
        print("**********",category)
        c = Category.objects.get(pk=category)
        products = Product(category=c, name=name, image=image)
        products.save()
        return redirect('productlist')

    return render(request, 'add_product.html',{'categories': categories, })




def EditProduct(request, id):
    cat = Category.objects.all()
    prod = Product.objects.get(pk=id)

    context = {
        'cat': cat,
        'prod':prod,
    }
    return render(request, 'update_product.html',context)



def UpdateProduct(request, id):

    category = request.POST.get('selected_cat', False)
    name = request.POST.get('name', False)
    image = request.FILES.get('image', False)

    print("******",category)
    cat = Category.objects.get(pk=category)
    prod = Product.objects.get(pk=id)
    prod.category = cat
    prod.name = name
    
    if image != False:
        prod.image = image

    prod.save()


    return redirect('productlist')




