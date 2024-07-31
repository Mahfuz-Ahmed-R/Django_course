from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from library_management import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('core/', include('core.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)