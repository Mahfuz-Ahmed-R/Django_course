from django.urls import  path
from . import views

urlpatterns = [
    path('show/', views.show_tasks, name='show_tasks'),
]
