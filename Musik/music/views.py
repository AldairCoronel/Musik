from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
from music.models import Song

# Create your views here.

# def index(request):
#     """Music index.
#
#     Showing welcome message
#     """
#     template = "music/index.html"
#     return render(request, template)
#
# def top_songs(request):
#     """Top songs.
#
#     TODO: Showing songs by its popularity
#     """
#     template = "music/top_songs.html"
#     return render(request, template)

# Class based views.

class Index(View):
    """Music index.

    Showing welcome message
    """
    template = "music/index.html"
    def get(self, request):
        "GET"
        return render(request, self.template)


class TopSongs(View):
    """Top songs.

    TODO: Showing songs by its popularity
    """
    template = "music/top_songs.html"
    def get(self, request):
        """GET method."""
        songs = Song.objects.all()
        context = {"songs": songs}
        for song in songs:
            print(song.song_file)
        return render(request, self.template, context)
