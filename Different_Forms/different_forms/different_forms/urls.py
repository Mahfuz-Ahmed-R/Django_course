from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="homepage"),
    path("contact/", views.contact, name="contact"),
]
