from django.urls import path
from . import apis 
from . import views


urlpatterns = [
    path('create/', apis.create_order),
    path('append/address/', apis.add_address),
    path('append/datetime/', apis.add_datetime),
    path('payment/', apis.finalize_order),
    path('list/', apis.load_many_orders),
    path('<int:pk>/', apis.load_one_order),

    path('order/', views.OrderView, name="order"),
    path('add_order/', views.AddOrder, name="add_order"),
    path('order/delete/<int:id>', views.DeleteOrder, name='delete'),
    path('order/update/<int:id>', views.UpdateOrder, name='update'),
    path('order/update/updateorder/<int:id>', views.UpdateRecords, name='updaterecord'),
    
]