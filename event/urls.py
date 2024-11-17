from django.urls import path
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()

router.register(r'event',EventViewSet,basename = "event")
router.register(r'participant',ParticipantViewSet, basename = 'participant')

urlpatterns = router.urls+[
    
]
