from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="homepage"),
    # path('esset/', views.EssetView, name="esset"),
    path('products/<int:cat_id>/', views.ProductsView, name="products"),
    # path('sad/<int:n>/', views.sad, name="sad"),
    path('register/',views.Register ,name='register'),
    path('login/',views.Login ,name='login'),
    path('logout/',views.Logout ,name='logout'),
    path('order/', views.OrderView, name="order"),
    path('add_order/', views.AddOrder, name="add_order"),
    path('order/delete/<int:id>', views.DeleteOrder, name='delete'),
    path('order/update/<int:id>', views.UpdateOrder, name='update'),
    path('order/update/updateorder/<int:id>', views.UpdateRecords, name='updaterecord'),




]