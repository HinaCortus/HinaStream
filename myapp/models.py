# myapp/models.py
from django.db import models
from django.contrib.auth.models import User

class AudioRecording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"AudioRecording {self.id} by {self.user.username}"

class ExtractedWord(models.Model):
    audio_recording = models.ForeignKey(AudioRecording, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word

class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.action} - {self.timestamp}"

class Announcement(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.id
