from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Book)
admin.site.register(models.Category)
admin.site.register(models.Transaction)
admin.site.register(models.Review)
