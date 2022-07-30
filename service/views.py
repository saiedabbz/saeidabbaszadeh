from django.shortcuts import render
from . models import Service


# def ServiceView(request):
#     services = Service.objects.all()
#     context = {
#         'services': services
#     }
#     return render(request, 'index.html' , context)