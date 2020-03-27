from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('top_songs', views.TopSongs.as_view(), name='top_songs'),
    path('artist/create-artist', views.CreateArtist.as_view(), name='create_art'),
]
