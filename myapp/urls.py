# myapp/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AudioRecordingViewSet, ExtractedWordViewSet, UserLogViewSet, 
    AnnouncementViewSet, MapPointViewSet, home
)

router = DefaultRouter()
router.register(r'audio-recordings', AudioRecordingViewSet)
router.register(r'extracted-words', ExtractedWordViewSet)
router.register(r'user-logs', UserLogViewSet)
router.register(r'announcements', AnnouncementViewSet)
router.register(r'map-points', MapPointViewSet, basename='map-points')

urlpatterns = [
    path('', home, name='home'),
    path('api/', include(router.urls)),
]
