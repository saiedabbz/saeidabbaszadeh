from django.urls import path
from . import views

urlpatterns = [
    
    path('customer_list/', views.CustomerList, name='customerlist'),
    path('add_customer/',views.AddCustomer, name="add_customer"),
    path('customer_list/delete/<int:id>', views.DeleteCustomer, name='delete'),
    path('customer_list/update/<int:id>',views.UpdateCustomer, name="update"),
    path('customer_list/update/updatecustomer/<int:id>', views.UpdateCustomerRecord, name="update_customer_record"),


]