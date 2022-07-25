from django.urls import path
from . import views

urlpatterns = [
    
    path('order/', views.OrderView, name="order"),
    path('add_order/', views.AddOrder, name="add_order"),
    path('order/delete/<int:id>', views.DeleteOrder, name='delete'),
    path('order/update/<int:id>', views.UpdateOrder, name='update'),
    path('order/update/updateorder/<int:id>', views.UpdateRecords, name='updaterecord'),
    
]