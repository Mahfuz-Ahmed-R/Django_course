from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('task_category/', include('task_category.urls')),
    path('task_model/', include('task_model.urls')),
    path('show_tasks/', include('show_tasks.urls')),
]
