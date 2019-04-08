from django import forms
from .models import Artist
import datetime

class searchForm(forms.Form):
    class Meta:
        model = Artist
        fiels = ['name','DOB','Genre',]

    # artist_name = forms.CharField(label='Arist Name', max_length = 20)
    # DOB = forms.DateField(input_formats='%d/%m/%Y')

        