from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='register'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.UserDetailsChange.as_view(), name='edit_profile'),
    path('password/', views.PasswordView.as_view(), name='password'),
    path('buy_car/<int:id>/', views.buy_car, name='buy_car'),
    # path('purchase_history/', views.purchase_history, name='purchase_history'),
    path('addcar/', views.add_car, name='car'),
]