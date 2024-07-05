from django.urls import  path
from album_model import views

urlpatterns = [
    path('add/', views.AddAlbumCreateView.as_view(), name='add_album'),
    path('edit/<int:id>/', views.EditAlbumUpdateView.as_view(), name='edit'),
]
