from django.urls import path
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import WatchListAV, WatchDetailsAV, StreamPlatformAV

urlpatterns = [
    path('list/',  WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='watch_details'),
    
    path('stream/', StreamPlatformAV.as_view(), name='stream'), 
]
