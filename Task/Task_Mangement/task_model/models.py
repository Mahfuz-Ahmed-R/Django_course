from task_category.models import CategoryModel
from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    categories = models.ManyToManyField(CategoryModel)
    Complete = models.BooleanField(default=False)
    date_field = models.DateTimeField()

    def __str__(self):
        return self.title