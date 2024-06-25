from django.db import models
from musician_model.models import MusicModel

# Create your models here.
class AlbumModel(models.Model):
    author = models.ForeignKey(MusicModel, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=20)
    album_release_date = models.DateTimeField()
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]
    album_rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.album_name