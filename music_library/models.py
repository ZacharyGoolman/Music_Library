from django.db import models

# Create your models here.
# Once your model is created move to serializer

class Song(models.Model):
    title = models.CharField(max_length=300)
    artist = models.CharField(max_length=300)
    album = models.CharField(max_length=300)
    release_date = models.DateField()
    genre = models.CharField(max_length=300)
    like = models.IntegerField(default=0)