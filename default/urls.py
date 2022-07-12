from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('products/<int:cat_id>/', views.ProductsView, name="products"),

    path('register/',views.Register ,name='register'),
    path('login/',views.Login ,name='login'),
    path('logout/',views.Logout ,name='logout'),

    path('order/', views.OrderView, name="order"),
    path('add_order/', views.AddOrder, name="add_order"),
    path('order/delete/<int:id>', views.DeleteOrder, name='delete'),
    path('order/update/<int:id>', views.UpdateOrder, name='update'),
    path('order/update/updateorder/<int:id>', views.UpdateRecords, name='updaterecord'),

    path('customer_list/', views.CustomerList, name='customerlist'),
    path('add_customer/',views.AddCustomer, name="add_customer"),
    path('customer_list/delete/<int:id>', views.DeleteCustomer, name='delete'),
    path('customer_list/update/<int:id>',views.UpdateCustomer, name="update"),
    path('customer_list/update/updatecustomer/<int:id>', views.UpdateCustomerRecord, name="update_customer_record"),

    path('products/', views.ProductList, name="productlist"),
    path('products/delete/<int:id>/', views.DeleteProduct , name="delete_product"),
    path('add_product/', views.AddProduct, name="add_product"),




]