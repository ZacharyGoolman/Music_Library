from dataclasses import fields
from rest_framework import serializers      
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'media', 'title', 'artist','album', 'release_date', 'genre', 'like']