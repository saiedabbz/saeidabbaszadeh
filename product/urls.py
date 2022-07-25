from django.urls import path
from . import apis 
from . import views

urlpatterns = [
    path('', apis.home_page),
    path('collections/', apis.load_collections),
    path('api/products/', apis.load_products),
    path('product/<slug:product_slug>/', apis.load_product_detail),
    path('eset/list/', apis.eset_list, name='eset_list'),
    path('eset/detail/', apis.eset_detail, name='eset_detail'),
    path('kaspersky/list/', apis.kaspersky_list, name='kaspersky_list'),
    path('kaspersky/detail/', apis.kaspersky_detail, name='kaspersky_detail'),

    path('products/', views.ProductList, name="productlist"),
    path('add_product/', views.AddProduct, name="add_product"),
    path('products/delete/<int:id>', views.DeleteProduct , name="delete_product"),
    path('products/update/<int:id>/', views.EditProduct, name="edit_product"),
    path('products/update/updateproduct/<int:id>',views.UpdateProduct, name="updateproduct"),
]
