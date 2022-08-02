from django.shortcuts import render
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    print(movies)
