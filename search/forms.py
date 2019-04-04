from django import forms

class searchForm(forms.Form):
    artist_name = forms.CharField(label='Arist Name', max_length = 30)
        