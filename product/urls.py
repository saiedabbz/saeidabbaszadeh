from django.urls import path
from . import views

urlpatterns = [

    path('products/', views.ProductList, name="productlist"),
    path('add_product/', views.AddProduct, name="add_product"),
    path('products/delete/<int:id>', views.DeleteProduct , name="delete_product"),
    path('products/update/<int:id>/', views.EditProduct, name="edit_product"),
    path('products/update/updateproduct/<int:id>',views.UpdateProduct, name="updateproduct"),

]