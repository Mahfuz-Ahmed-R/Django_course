from django.urls import path
from . import views

urlpatterns = [
    path('show/', views.models, name='all_models'),
]
