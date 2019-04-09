from django.db import models
import datetime

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    DOB = models.DateField(auto_now=False,default=datetime.date.today)
    SSN = models.CharField(max_length=9)
    monthly_views = models.IntegerField(default=-1)
    Genre = models.CharField(max_length = 15)
    label_rank = models.IntegerField(default=-1)

    def __str__(self):
        return self.name

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=25)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    label = models.CharField(max_length=25)
    sales = models.IntegerField(default=-1)
    year = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    song_id = models.IntegerField(primary_key=True)
    track = models.CharField(max_length=25)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    length = models.DateTimeField(default=datetime.date.today)
    streams = models.IntegerField(default=-1)
    featured = models.ForeignKey(Artist,null=True,related_name="featured_artist",on_delete=models.CASCADE)

    def __str__(self):
        return self.track
