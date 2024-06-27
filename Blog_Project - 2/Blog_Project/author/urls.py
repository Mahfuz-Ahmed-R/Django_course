from django.urls import  path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
    path('edit_profile/', views.edit_profile, name = 'edit_profile'),
    path('profile/passwordChange/', views.passwordChange, name = 'passwordChange'),
    path('logout/', views.user_logout, name = 'logout'),
]
