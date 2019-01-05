# # # -*- coding: utf-8 -*-
# # from __future__ import unicode_literals

 

# # # Create your views here.

# from django.shortcuts import render, get_object_or_404
# # from django.http import HttpResponse
# from .models import Album, Song
# # from django.http import Http404
# # from django.template import loader



# def index(request):
#     all_albums = Album.objects.all()
#     return render(request,'music/index.html',{'all_albums': all_albums})


# def detail(request, album_id):
#     # return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
#     # try:
#     #     album = Album.objects.get(pk=album_id)
#     # except Album.DoesNotExist:
#     #     raise Http404("Album does  not exist")
#     album = get_object_or_404(Album, pk = album_id)
#     return render(request,'music/detail.html',{'album': album})

# def favorite(request, album_id):
#     album = get_object_or_404(Album, pk = album_id)
#     try:
#         selected_song = album.song_set.get(pk = request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request,'music/detail.html',{
#             'album': album,
#             'error_message' : "You didnt select the valid song"
#             })
#     else:   
#         selected_song.is_favorite = True
#         selected_song.save()
#         return render(request,'music/detail.html',{'album': album})

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()
    
class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(generic.CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']