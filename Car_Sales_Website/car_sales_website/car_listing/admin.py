from django.contrib import admin
from .models import CarBrand

# Register your models here.
class CarBrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']
    search_fields = ['name']

admin.site.register(CarBrand, CarBrandAdmin)