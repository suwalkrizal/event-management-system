from django.shortcuts import render
from .models import *
from rest_framework import viewsets, filters
from .serializer import EventSerializer, ParticipantSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



# Create your views here.

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ('title',)
    search_fields = ('title',)
    
class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,DjangoFilterBackend)
    filterset_fields = ('event',)
    search_fields = ('event',)