#  from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist, Song, Lyric
from .serializers import ArtistSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def artist_list(request): 
    
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse({'artists':serializer.data}, safe=False)

    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
def song_list(request): 
    
    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JsonResponse({'songs':serializer.data}, safe=False)
    
def lyric_list(request): 
    
    if request.method == 'GET':
        lyrics = Lyric.objects.all()
        serializer = LyricSerializer(lyrics, many=True)
        return JsonResponse({'lyrics':serializer.data}, safe=False)
    
@api_view(['GET', 'PUT', 'DELETE'])      
def song_detail(request, id):
        
        try:
            song = Song.objects.get(pk=id)
        except Song.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = SongSerializer(song)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = SongSerializer(song, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    #     songs = Artist.objects.all()
    #     serializer = SongSerializer(songs, many=True)
    #     return JsonResponse({'songs':serializer.data}, safe=False)

    # def lyric_list(request):
    #     lyrics = Lyric.objects.all()
    #     serializer = LyricSerializer(lyrics, many=True)
    #     return JsonResponse({'lyrics':serializer.data}, safe=False)
