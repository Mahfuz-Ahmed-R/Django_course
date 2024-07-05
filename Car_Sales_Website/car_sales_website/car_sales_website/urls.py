from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'homepage'),
    path('brand/<slug:brand_slug>', views.home, name='brand_wise_post'),
    path('car/', include('car.urls')),
    path('car_listing/', include('car_listing.urls')),
    path('details/<int:id>/', views.DetailedView.as_view(), name='details'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)