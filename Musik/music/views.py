from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.template import loader

# Create your views here.

def index(request):
    """Music index.

    Showing welcome message
    """
    template = "music/index.html"
    return render(request, template)

def top_songs(request):
    """Top songs.

    TODO: Show songs by its popularity
    """
    return HttpResponse(
        "<head><title>Canciones populares</title></head>"
        "<body><h1>Estas son las canciones del momento:</h1></body>"
    )
