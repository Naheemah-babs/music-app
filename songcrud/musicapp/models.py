from datetime import datetime
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name=models.CharField(max_length=400)
    last_name=models.CharField(max_length=400)
    age=models.IntegerField(default=0)

    def __str__(self):
        return self.first_name
    
class Song(models.Model):
    artist_id=models.ForeignKey(Artist, on_delete=models.CASCADE)
    title=models.CharField(max_length=1000  )
    date_released=models.DateField(default=datetime.today)
    likes=models.IntegerField()

    def __str__(self):
        return self.title 
     
class Lyric(models.Model):
    content=models.CharField(max_length=4000)
    song_id=models.ForeignKey(Song, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.content