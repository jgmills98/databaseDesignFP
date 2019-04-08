from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import searchForm
from .models import Artist

from django.db.models import Q

def home(request):

    form = searchForm()
    artist = Artist.objects.get(pk=1)
    form = searchForm(instance=artist)

    return render(request,'search/home.html',{'form':searchForm()})

def test(request):
    return render(request,'search/test.html')

def result(request):
    if request.method == "GET":
        form = request.GET
        form = form.copy()

        form.pop('csrfmiddlewaretoken')

        # query = Artist.objects.raw('select * from project_artist;')
        print(form.__contains__("artist_name"))


        query = Artist.objects.filter(name__iexact=form['artist_name'])

        result = [entry for entry in query.values()]
        # print(query.values())
        # print(type(lis))
        queryRes = {
            'result':result
        }

        # print(Artist.objects.filter(name='lil Wayne')[0].DOB)
    return render(request,'search/result.html',queryRes)
