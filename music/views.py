# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

 

# # Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.http import Http404
#from django.template import loader



def index(request):
    all_albums = Album.objects.all()
    return render(request,'music/index.html',{'all_albums': all_albums})


def detail(request, album_id):
    # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does  not exist")
    return render(request,'music/detail.html',{'album': album})
