from django.urls import path
from .views import UserDeposit, Borrow

urlpatterns = [
    path('deposit/', UserDeposit.as_view(), name = 'deposit'),
    path('borrow/<int:id>', Borrow.as_view(), name = 'borrow'),
]
