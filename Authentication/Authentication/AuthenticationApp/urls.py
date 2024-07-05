from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrationPage, name = 'register'),
    path('login/', views.user_login, name = 'login'),
    path('logout/', views.user_logout, name = 'logout'),
    path('profile/', views.edit_profile, name = 'profile'),
    path('password/', views.password_change, name = 'password_change'),
    path('password_without_old/', views.password_change_without_old, name = 'pass_change_without_old_pass'),
]
