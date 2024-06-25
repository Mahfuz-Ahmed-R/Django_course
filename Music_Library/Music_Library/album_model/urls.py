from django.urls import  path
from album_model import views

urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('edit/<int:id>', views.edit_album, name='edit'),
]
