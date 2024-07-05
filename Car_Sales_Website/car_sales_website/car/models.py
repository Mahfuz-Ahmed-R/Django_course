from django.db import models
from car_listing.models import CarBrand
from car_sales_website import settings

# Create your models here.
class CarModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank = True, null = True)
    
    
    def __str__(self):
        return self.name

class Purchase(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by{self.name}"
