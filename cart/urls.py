from django.urls import path
from . import views 


urlpatterns = [
    path('', views.cart),
    path('item/', views.set_cart_item),
    path('add/items/', views.set_cart_items),
]

