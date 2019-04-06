from django import forms
import datetime

class searchForm(forms.Form):
    artist_name = forms.CharField(label='Arist Name', max_length = 20)
    dob = forms.DateField(input_formats='%d/%m/%Y')

        