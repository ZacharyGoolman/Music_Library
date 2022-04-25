from pydoc import resolve
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer
from .models import Song
from rest_framework import status

# Create your views here.


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

# @api_view(['GET',])          
     