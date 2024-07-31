from django.urls import path
from .views import RegistrationView, UserLoginView, UserLogout, profile

urlpatterns = [
    path('register/', RegistrationView.as_view(), name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('logout/', UserLogout.as_view(), name = 'logout'),
    path('profile/', profile, name = 'profile'),
]
