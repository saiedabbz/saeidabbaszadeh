from django.urls import path
from . import views
from . import apis

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('products/<slug:slug>/', views.ProductsView, name="products"),
    path('service/<int:id>/', views.ServiceView, name="service"),



    path('category/', views.Categories, name="category_list"),
    path('category/delete/<int:id>', views.Delete, name="delete_category"),
    path('add_category/', views.AddCategory, name="add_category"),
    path('category/update/<int:id>', views.EditCategory, name="edit_category"),
    path('category/update/updatecategory/<int:id>', views.UpdateCategory , name="update_category"),


    path('product/<slug:pro_slug>/', views.ProductDetail, name="eset"),

    path('service/<int:id>', views.ServiceView, name="services"),
]