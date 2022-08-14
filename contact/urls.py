from django.urls import path
# from . import apis 
from . import views

urlpatterns = [
    path('add_inquery/<slug:slug>/', views.addInquery, name="add_inquery"),
    path('insert_inquery/<slug:slug>/', views.insertInquery, name="insert_inquery"),
]