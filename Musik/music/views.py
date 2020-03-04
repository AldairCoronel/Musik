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
    template = "music/top_songs.html"
    return render(request, template)
