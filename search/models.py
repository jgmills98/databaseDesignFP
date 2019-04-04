from django.db import models
import datetime

class Artist(models.Model):
    name = models.CharField(max_length=25)
    DOB = models.DateField(auto_now=False,default=datetime.date.today)
    SSN = models.CharField(max_length=9)
    monthly_views = models.IntegerField(default=-1)
    Genre = models.CharField(max_length = 15)
    label_rank = models.IntegerField(default=-1)

    def __str__(self):
        return self.name