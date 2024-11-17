from rest_framework import serializers
from .models import *

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'title', 
            'description', 
            'location', 
            'start_time', 
            'end_time', 
            'is_active',   
        )
        model = Event
        
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'event', 
            'name', 
            'email', 
            'register_at',
        )
        
    model = Participant