from datetime import datetime
from time import timezone
from django.db import models

# Create your models here.
class NsuBinModel(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)

    def __str__(self):
        return self.name