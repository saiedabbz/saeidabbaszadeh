from django.urls import path
from . import views 


urlpatterns = [
    path('bank/<slug:transaction_id>/', views.bank_callback),
]

