from django.urls import path
from . import views 


urlpatterns = [
    path('auth/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),

    path('signup/', views.signup),
    path('addresses/', views.load_addresses),
    path('add-address/', views.add_address),
    path('data/', views.UserAPI.as_view()),
    path('address/<int:pk>/', views.AddressAPI.as_view()),
]


