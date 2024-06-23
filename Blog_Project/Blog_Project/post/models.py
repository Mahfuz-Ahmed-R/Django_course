from django.db import models
from catagories.models import Categorice
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    category = models.ManyToManyField(Categorice)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title