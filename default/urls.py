from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    path('esset/', views.EssetView, name="esset"),
]