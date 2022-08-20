from django.urls import path
# from . import apis 
from . import views

urlpatterns = [
    path('add_inquery/<slug:slug>/', views.addInquery, name="add_inquery"),
    path('insert_inquery/<slug:slug>/', views.insertInquery, name="insert_inquery"),
    path('contact_us/', views.addContactUs, name="contact_us"),
    path('insert_contact_us/', views.insertContactUs, name="insert_contactus"),
    path('insert_contact_us/success/', views.success, name="success"),

    
]