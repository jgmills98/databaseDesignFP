from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,QueryDict
from .forms import artistForm,albumForm,songForm
from .models import Artist,Album,Song
from django.db.models.query import QuerySet

from django.db.models import Q

def home(request):

    # form = artistForm()
    # artist = Artist.objects.get(pk=1)
    # form = searchForm(instance=artist)

    return render(request,'search/home.html',{'artistForm':artistForm(),'albumForm':albumForm(),'songForm':songForm()})

def test(request):
    return render(request,'search/test.html')

def result(request):
    if request.method == "GET":
        form = request.GET #get form from GET request
        form = form.copy()
        form.pop('csrfmiddlewaretoken') #remove token from request
        # print(form)
        # form.pop('artistSearch')
        
        artistQuery,albumQuery,songQuery = formatQuery(request,form)#create 3 sub queries

        # artists,albums,songs = QuerySet()
        print(artistQuery)
        print(albumQuery)
        print(songQuery)
        
        if form.__contains__('all'):
            print(form.__contains__('all'))
        elif form.__contains__('artistSearch'):
            if(bool(artistQuery)):
                artists = Artist.objects.filter(**artistQuery.dict())
            else:
                artists = Artist.objects.none()

            if(bool(albumQuery)):
                albums = Album.objects.filter(**albumQuery.dict())
                if(bool(artists)):
                    artists = artists.filter(artist_id__in=albums.values_list('artist_id')).select_related()
                else:
                    artists = Artist.objects.filter(artist_id__in=albums.values_list('artist_id')).select_related()
            else:
                albums = Album.objects.none()

            if bool(songQuery):
                songs = Song.objects.filter(**songQuery.dict())

                if(bool(artists)):
                    artists = artists.filter(artist_id__in=songs.values_list('artist_id')).select_related()
                else:
                    artists = Artist.objects.filter(artist_id__in=songs.values_list('artist_id')).select_related()


            else:
                songs = Song.objects.none()
            
            # print(artistQuery)
            # print(albumQuery)
            # print(songQuery)
            print(artists)
            print(albums)
            print(songs)

        # print(bool(artistQuery))
        # if not bool(artistQuery):
        #     artists = Artist.objects.filter(**artistQuery.dict())

# Album.objects.filter(artist__in=a.values_list('artist_id')).select_related()

        query = Artist.objects.filter(**artistQuery.dict())
        
        result = [entry for entry in artists.values()]

        queryRes = {
            'artistResult':[entry for entry in artists.values()],
            'albumResult':[entry for entry in albums.values()],
            'songResult':[entry for entry in songs.values()]
        }
        # print(queryRes)



        # print(Artist.objects.filter(name='lil Wayne')[0].DOB)
    return render(request,'search/result.html',queryRes)

def formatQuery(request,form):

    artistQuery = QueryDict().copy()
    albumQuery = QueryDict().copy()
    songQuery = QueryDict().copy()
    
    #format artist query
    if form.get('name') != "":
        artistQuery.appendlist('name',form.get('name'))
    if form.get('DOB') != "":
        artistQuery.appendlist('DOB',form.get('DOB'))
    if form.get('Genre') != "":
        artistQuery.appendlist('Genre',form.get('Genre'))
    if form.get('monthly_views') != "":
        artistQuery.appendlist('monthly_views',form.get('monthly_views'))
    
    #format album query

    if form.get('title') != "":
        albumQuery.appendlist('title',form.get('title'))
    if form.getlist('artist')[0] != "":
        albumQuery.appendlist('artist',form.getlist('artist')[0])
    if form.get('label') != "":
        albumQuery.appendlist('label',form.get('label'))        
    if form.get('sales') != "":
        albumQuery.appendlist('sales',form.get('sales'))
    if form.get('year') != "":
        albumQuery.appendlist('year',form.get('year'))


    #formatsong query
    if form.get('track') != "":
        songQuery.appendlist('track',form.get('track'))
    if form.get('album') != "":
        songQuery.appendlist('album',form.get('album'))
    if form.getlist('artist')[1] != "":
        albumQuery.appendlist('artist',form.getlist('artist')[1])
    if form.get('length') != "":
        songQuery.appendlist('length',form.get('length'))        
    if form.get('streams') != "":
        songQuery.appendlist('streams',form.get('streams'))
    if form.get('featured') != "":
        songQuery.appendlist('featured',form.get('featured'))

    # print(artistQuery.__contains__('name'))

    return artistQuery,albumQuery,songQuery

        