from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader
from .models import Song

# Create your views here.

def index(request):
    """Music index.

    Showing welcome message
    """
    template = "music/index.html"
    return render(request, template)

def top_songs(request):
    """Top songs.

    TODO: Showing songs by its popularity
    """
    template = "music/top_songs.html"
    return render(request, template)

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
        to_play_id = request.GET.get("to_play", 1)
        songs_to_play = Song.objects.filter(id = to_play_id)
        if songs_to_play.count() == 0:
            to_play = Song.objects.first()
        else:
            to_play = songs_to_play.first()

        context = {"songs": songs, "to_play": to_play}
        return render(request, self.template, context)
