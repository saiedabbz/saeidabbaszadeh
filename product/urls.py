from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductView, name="product_index"),
]