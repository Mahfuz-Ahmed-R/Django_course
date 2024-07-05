from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.car_list, name='carlist'),
]