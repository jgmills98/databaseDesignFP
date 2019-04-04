from django.shortcuts import render
from django.http import HttpResponse

artists = [
    {
        'artist': 'lil wayne',
        'address': 'xd lol'
    },
    {
        'artist': 'hehehe',
        'address': 'ok xd 123'
    },

]

def home(request):
    context = {
        'artists': artists
    }
    # if(request.GET.get('searchButton')):
    #     print("xd")

    return render(request,'search/base.html',context)

def test(request):
    return render(request,'search/test.html')



