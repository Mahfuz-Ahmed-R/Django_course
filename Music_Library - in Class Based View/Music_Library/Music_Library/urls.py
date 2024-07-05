from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('musician_model/', include('musician_model.urls')),
    path('album_model/', include('album_model.urls')),
]
