from django import forms
from .models import Artist,Album,Song
import datetime

class artistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name','DOB','Genre','monthly_views']

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title','artist','label','sales','year']

class songForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['track','album','artist','length','streams','featured']