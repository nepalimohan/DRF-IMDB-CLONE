from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_details, movie_list
from watchlist_app.api.views import (WatchListAV, WatchDetailsAV, StreamPlatformAV, ReviewCreate,
                                     StreamPlatformDetailAV, ReviewList, ReviewDetails, StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
#using router, you dont need to speciy stream/<int:pk> urls, the above will work for both

urlpatterns = [
    path('list/',  WatchListAV.as_view(), name='watch_list'),
    path('<int:pk>', WatchDetailsAV.as_view(), name='watch_details'),
    
    # path('stream/', StreamPlatformAV.as_view(), name='stream'), 
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_details'), 
    
    path('', include(router.urls)),
    
    # path('review', ReviewList.as_view(), name= "review-list"),
    # path('review/<int:pk>', ReviewDetails.as_view(), name= "review-details"),
    
    
    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetails.as_view(), name= "review-details"),
    
]
