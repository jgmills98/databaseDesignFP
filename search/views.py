from django.shortcuts import render
from django.http import HttpResponse,JsonResponse



artists = [
    {
        'artist': 'lil wayne',
        'address': 'xd lol'
    },
    {
        'artist': 'bruno mars',
        'address': 'ok xd 123'
    },

]

kk = "hello test world"

def home(request):
    context = {
        'artists': artists
    }
    # if(request.GET.get('searchButton')):
    #     print("xd")

    return render(request,'search/base.html',context)

def test(request):
    return render(request,'search/test.html')

def validate_username(request):
    # console.log('here')
    artistName = request.GET.get('artistName')
    songName = request.GET.get('songName')
    data = {
        'dat':songName+'testtest',
        'xd':artistName
    }
    return JsonResponse(data)


    

    



