from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('products/<int:cat_id>/', views.ProductsView, name="products"),

    path('register/',views.Register ,name='register'),
    path('login/',views.Login ,name='login'),
    # path('logout/',views.Logout ,name='logout'),

    path('category/', views.Categories, name="category_list"),
    path('category/delete/<int:id>', views.Delete, name="delete_category"),
    path('add_category/', views.AddCategory, name="add_category"),
    path('category/update/<int:id>', views.EditCategory, name="edit_category"),
    path('category/update/updatecategory/<int:id>', views.UpdateCategory , name="update_category"),


    # path('api/category/', views.Categories, name="category_list"),
    # path('api/category/delete/<int:id>', views.Delete, name="delete_category"),
    # path('api/add_category/', views.AddCategory, name="add_category"),
    # path('api/category/update/<int:id>', views.EditCategory, name="edit_category"),
    # path('api/category/update/updatecategory/<int:id>', views.UpdateCategory , name="update_category"),



]