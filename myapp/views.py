# myapp/views.py
from django.shortcuts import render

from rest_framework import viewsets
from .models import AudioRecording, ExtractedWord, UserLog, Announcement
from .serializers import (
    AudioRecordingSerializer, ExtractedWordSerializer, UserLogSerializer, 
    AnnouncementSerializer, MapPointSerializer
)


### PARTIE FRONT ###
def home(request):

    return render(request, 'front/home.html', {})

### PARTIE API ###
class AudioRecordingViewSet(viewsets.ModelViewSet):
    queryset = AudioRecording.objects.all()
    serializer_class = AudioRecordingSerializer

class ExtractedWordViewSet(viewsets.ModelViewSet):
    queryset = ExtractedWord.objects.all()
    serializer_class = ExtractedWordSerializer

class UserLogViewSet(viewsets.ModelViewSet):
    queryset = UserLog.objects.all()
    serializer_class = UserLogSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

class MapPointViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = MapPointSerializer