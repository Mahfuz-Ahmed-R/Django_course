from django.db import models
from catagories.models import Categorice
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    category = models.ManyToManyField(Categorice)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title