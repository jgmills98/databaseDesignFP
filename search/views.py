from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,QueryDict
from .forms import artistForm,albumForm,songForm
from .models import Artist,Album,Song
from django.db.models.query import QuerySet

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from django.db.models import Q

def home(request):

    # form = artistForm()
    # artist = Artist.objects.get(pk=1)
    # form = searchForm(instance=artist)

    return render(request,'search/home.html',{'artistForm':artistForm(),'albumForm':albumForm(),'songForm':songForm()})

def test(request):
    return render(request,'search/test.html')

def result(request):
    print(request.user.groups.all()[0].name)
    if request.method == "GET":
        form = request.GET #get form from GET request
        form = form.copy()
        form.pop('csrfmiddlewaretoken') #remove token from request
        # print(form)
        # form.pop('artistSearch')
        
        artistQuery,albumQuery,songQuery = formatQuery(request,form)#create 3 sub queries

        
        if form.__contains__('allSearch'):  
            queryRes = makeQuery(artistQuery,albumQuery,songQuery,0)
        elif form.__contains__('artistSearch'):
            queryRes = makeQuery(artistQuery,albumQuery,songQuery,1)
        elif form.__contains__('albumSearch'):
            queryRes = makeQuery(artistQuery,albumQuery,songQuery,2)
        elif form.__contains__('songSearch'):
            queryRes = makeQuery(artistQuery,albumQuery,songQuery,3)

        if request.user.groups.all()[0].name == 'Listener':
            for val in queryRes['artistResult']:
                del val['SSN']
                del val['monthly_views']
                del val['label_rank']
            for val in queryRes['albumResult']:
                del val['sales']
                del val['album_id']
            for val in queryRes['songResult']:
                del val['streams']
                del val['song_id']

        elif request.user.groups.all()[0].name == 'Label':
            for val in queryRes['albumResult']:
                del val['album_id']
            for val in queryRes['songResult']:
                del val['song_id']

        elif request.user.groups.all()[0].name == 'Service':
            for val in queryRes['artistResult']:
                del val['SSN']
                del val['label_rank']            
        
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

def artistSearch(artistQuery,albumQuery,songQuery):
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
    
    queryRes = {
            'artistResult':[entry for entry in artists.values()],
            'albumResult':[entry for entry in albums.values()],
            'songResult':[entry for entry in songs.values()]
        }

    # print(queryRes)

    return queryRes     

def albumSearch(artistQuery,albumQuery,songQuery):
    if(bool(albumQuery)):
        albums = Album.objects.filter(**albumQuery.dict())
    else:
        albums = Album.objects.none()
    
    if(bool(artistQuery)):
        artists = Artist.objects.filter(**artistQuery.dict())

        if(bool(albums)):
            # albums = albums.filter(artist_id__in=)
            albums = albums.filter(artist_id__in=artists.values_list('artist_id')).select_related()
        else:
            albums = Album.objects.filter(artist_id__in=artists.values_list('artist_id')).select_related()

    else:
       artists = Artist.objects.none() 
    
    if(bool(songQuery)):
        songs = Song.objects.filter(**songQuery.dict())

        if(bool(albums)):
            # albums = albums.filter(artist_id__in=)
            albums = albums.filter(artist_id__in=songs.values_list('artist_id')).select_related()
        else:
            albums = Album.objects.filter(artist_id__in=songs.values_list('artist_id')).select_related()

    else:
        songs = Song.objects.none()

    queryRes = {
            'artistResult':[entry for entry in artists.values()],
            'albumResult':[entry for entry in albums.values()],
            'songResult':[entry for entry in songs.values()]
        }
    
    print(queryRes)

    return queryRes 


def makeQuery(artistQuery,albumQuery,songQuery,type):
    if( not bool(artistQuery) and not bool(albumQuery) and not bool(songQuery)):
        finalArtist = Artist.objects.all()
        finalAlbum = Album.objects.all()
        finalSong = Song.objects.all()
    else:
        artist1 = Artist.objects.filter(artist_id__in=Song.objects.filter(**songQuery.dict()).values_list('artist_id')).select_related()
        artist2 = Artist.objects.filter(artist_id__in=Album.objects.filter(**albumQuery.dict()).values_list('artist_id')).select_related()
        artist3 = artist1.filter(artist_id__in=artist2.values_list('artist_id')).select_related()
        finalArtist = artist3.filter(**artistQuery.dict())

        album1 = Album.objects.filter(album_id__in=Song.objects.filter(**songQuery.dict()).values_list('album_id')).select_related()
        album2 = Album.objects.filter(artist_id__in=Artist.objects.filter(**artistQuery.dict()).values_list('artist_id')).select_related()
        album3 = album1.filter(artist_id__in=album2.values_list('artist_id')).select_related()
        finalAlbum = album3.filter(**albumQuery.dict())

        song1 = Song.objects.filter(artist_id__in=Artist.objects.filter(**artistQuery.dict()).values_list('artist_id')).select_related()
        song2 = Song.objects.filter(artist_id__in=Album.objects.filter(**albumQuery.dict()).values_list('artist_id')).select_related()
        song3 = song1.filter(artist_id__in=song2.values_list('artist_id')).select_related()
        finalSong = song3.filter(**songQuery.dict())

    queryRes = {
            'artistResult':[entry for entry in finalArtist.values()],
            'albumResult':[entry for entry in finalAlbum.values()],
            'songResult':[entry for entry in finalSong.values()]
        }
    
    if type == 1:
        queryRes['albumResult'] = []
        queryRes['songResult'] = []
    elif type == 2:
        queryRes['artistResult'] = []
        queryRes['songResult'] = []
    elif type == 3:
        queryRes['artistResult'] = []
        queryRes['albumResult'] = []
    
    return queryRes
