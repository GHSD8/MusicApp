from django.shortcuts import redirect,render
from .models import Song

def index(request):
    song = Song.objects.all().order_by('title')
    song_list = list(Song.objects.all().order_by('title').values())
    context = {

        "songs": song,
        "songs_list": song_list,

    }
    return render(request ,'base.html' ,context)

def test(request):
    song = Song.objects.all().order_by('title')
    song_list = list(Song.objects.all().order_by('title').values())
    context = {

        "songs": song,
        "songs_list": song_list,

    }
    return render(request ,'index.html' ,context)
