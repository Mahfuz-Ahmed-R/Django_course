from django.db import models

# Create your models here.
class MusicModel(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField( max_length=254)
    phone = models.IntegerField()
    instrumentType = models.CharField(max_length=25)

    def __str__(self):
        return self.firstName