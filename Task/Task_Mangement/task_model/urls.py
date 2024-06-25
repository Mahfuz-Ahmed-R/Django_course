from django.urls import  path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>', views.edit_tasks, name='edit_tasks'),
    path('delete/<int:id>', views.delete_tasks, name='delete_tasks'),
]
