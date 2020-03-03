from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Music index.

    Showing welcome message
    """
    return HttpResponse("Welcome")

def top_songs(request):
    """Top songs.

    TODO: Show songs by its popularity
    """
    return HttpResponse(
        "<head><title>Canciones populares</title></head>"
        "<body><h1>Estas son las canciones del momento:</h1></body>"
    )
