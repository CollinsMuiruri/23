from django.shortcuts import render
from .models import *
from django.views import generic

# Create your views here.
class ArtistList(generic.ListView):
    queryset = Artist.objects.all()
    template_name = "artists.html"

class ArtistDetails(generic.DetailView):
    model = Artist
    template_name = "artistuno.html"