from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'homepage'),
    path('author/', include('author.urls')),
    path('catagories/', include('catagories.urls')),
    path('post/', include('post.urls')),
    path('profiles/', include('profiles.urls')),
]
