from os import stat
from re import A
from requests import delete
from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

#class based views
class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movies =  Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': 'Movie not found'}, status= status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movies)
        return Response(serializer.data)
    
    def put(self, request,pk):
        movies =  Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movies =  Movie.objects.get(pk=pk)
        movies.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

#function based views
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE']) 
# def movie_details(request,pk):
#     if request.method == 'GET':
#         try:
#             movies =  Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error': 'Movie not found'}, status= status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movies)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movies =  Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         movies =  Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
        