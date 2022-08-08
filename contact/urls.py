from django.urls import path
# from . import apis 
from . import views

urlpatterns = [
    path('add_inquery/<slug:slug>', views.InQuery, name="add_inquery"),
]