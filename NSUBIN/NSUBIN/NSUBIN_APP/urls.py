from django.urls import path
from .views import NsuBinView, NsuBinEditView

urlpatterns = [
    path('', NsuBinView.as_view(), name = 'nsubin'),
    path('edit/<int:pk>/', NsuBinEditView.as_view(), name = 'detailedview'),
]
