# Some imports auto populate and arent needed you can remove them if you want
from itertools import product
from urllib import response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SongSerializer
from .models import Song
from music_library import serializers



# Create your views here.
# Where we create basic CRUD functionality to test in postman
# This will tie into our front end

@api_view(['GET','POST']) 
def songs_list(request):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def music_detail(request, pk):

    songs = get_object_or_404(Song, pk=pk)

    if request.method == 'GET':
        serializer = SongSerializer(songs);
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SongSerializer(songs, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        custom_response = {'You have just removed': songs.title}
        songs.delete()
        return Response(custom_response, status=status.HTTP_204_NO_CONTENT)
        
# when applying patch in postman dont use a body
    elif request.method == 'PATCH':
         if songs.like >= 0:
            songs.like += 1
            serializer = SongSerializer(songs, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)    


                 
     