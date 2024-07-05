from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('add/', views.AddMusicianView.as_view(), name='add_musician'),
    path('edit/<int:id>/', views.EditView.as_view(), name='edit_musician'),
    path('delete/<int:id>/', views.DeleteMusicianView.as_view(), name='delete')
]