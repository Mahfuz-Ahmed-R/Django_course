from django.contrib import admin
from .models import CarModel, CommentModel, Purchase

# Register your models here.
admin.site.register(CarModel)
admin.site.register(CommentModel)
admin.site.register(Purchase)