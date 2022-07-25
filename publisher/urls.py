
from django.urls import path
from . import views

urlpatterns = [
    path('content/<int:id>/', views.content, name='content'),
    path('subscribe', views.subscribe, name='subscribe'),
]
