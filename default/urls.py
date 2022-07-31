from django.urls import path
from . import views
from . import apis

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('products/<int:cat_id>/', views.ProductsView, name="products"),

    # path('products/<int:id>', views.Navbar, name="navbar_view"),


    path('category/', views.Categories, name="category_list"),
    path('category/delete/<int:id>', views.Delete, name="delete_category"),
    path('add_category/', views.AddCategory, name="add_category"),
    path('category/update/<int:id>', views.EditCategory, name="edit_category"),
    path('category/update/updatecategory/<int:id>', views.UpdateCategory , name="update_category"),


    # path('products/eset_nod32/',views.EsetNod, name="eset_nod"),
    # path('products/eset_internet/', views.EsetInternet, name="eset_internet"),
    # path('products/eset_smart/', views.EsetSmart, name="eset_smart"),


    # path('products/2/<int:prod_id>', views.Kasper, name="kasper"),
    # path('products/6/<int:prod_id>', views.Eset, name="eset"),
    # path('product/<int:prod_id>', views.ProductDetail, name="eset"),
    path('product/<slug:pro_slug>/', views.ProductDetail, name="eset"),

    path('service/<int:id>', views.ServiceView, name="khadamat"),
]