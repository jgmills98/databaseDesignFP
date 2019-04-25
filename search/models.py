from django.db import models
import datetime

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25,blank=True)
    DOB = models.DateField(auto_now=False,blank=True)
    SSN = models.CharField(max_length=9,blank=True)
    monthly_views = models.IntegerField(blank=True)
    Genre = models.CharField(max_length = 15,blank=True)
    label_rank = models.IntegerField(blank=True)

    # def __str__(self):
    #     return self.name

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=25,blank=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,blank=True)
    label = models.CharField(max_length=25,blank=True)
    sales = models.IntegerField(blank=True)
    year = models.DateField(blank=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    song_id = models.IntegerField(primary_key=True)
    track = models.CharField(max_length=25,blank=True)
    album = models.ForeignKey(Album,on_delete=models.CASCADE,blank=True)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE,blank=True)
    length = models.DateTimeField(blank=True)
    streams = models.IntegerField(blank=True)
    featured = models.ForeignKey(Artist,null=True,blank=True,related_name="featured_artist",on_delete=models.CASCADE)

    def __str__(self):
        return self.track
        