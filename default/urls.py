from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    # path('esset/', views.EssetView, name="esset"),
    path('products/<int:cat_id>/', views.ProductsView, name="products"),
    # path('sad/<int:n>/', views.sad, name="sad"),
]