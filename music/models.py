from django.db import models

# Create your models here.
class Singer(models.Model):
    singer_id = models.CharField(max_length=100, primary_key=True)
    singer_name = models.CharField(max_length=100)
    summ = models.TextField()
    original_url = models.URLField()

class Song(models.Model):
    song_id = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    lyrics = models.TextField()
    original_url = models.URLField()

class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)