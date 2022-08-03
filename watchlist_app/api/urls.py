from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import MovieListAV, MovieDetailsAV

urlpatterns = [
    path('list/',  MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailsAV.as_view(), name='movie_details'),
]
