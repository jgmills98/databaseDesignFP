from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import searchForm
from .models import Artist



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
    form = searchForm()

    return render(request,'search/home.html',{'form':searchForm()})

def test(request):
    return render(request,'search/test.html')

def validate_username(request):
    print("request: ")
    print(request)
    artistName = request.GET.get('artistName')
    songName = request.GET.get('songName')
    data = {
        'dat':songName+'testtest',
        'xd':artistName
    }
    # return JsonResponse(data)
    return redirect('../result')

def result(request):
    if request.method == "GET":
        form = request.GET
        # print(type(form))
        print(form)
        query = Artist.objects.filter(name=form['artist_name'])
        lis = [entry for entry in query.values()]
        # print(query.values())
        print(lis)
        result = {
            'lis':lis
        }

        # print(Artist.objects.filter(name='lil Wayne')[0].DOB)
    return render(request,'search/result.html',result)
