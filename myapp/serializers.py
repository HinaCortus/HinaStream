# myapp/serializers.py

from rest_framework import serializers
from .models import AudioRecording, ExtractedWord, UserLog, Announcement

class AudioRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioRecording
        fields = '__all__'

class ExtractedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtractedWord
        fields = '__all__'

class UserLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLog
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class MapPointSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(source='latitude')
    longitude = serializers.FloatField(source='longitude')

    class Meta:
        model = Announcement
        fields = ('latitude', 'longitude')