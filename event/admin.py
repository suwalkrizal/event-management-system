from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'location', 'start_time', 'end_time', 'is_active',)
    search_fields = ('title',)
    list_filter = ('title',)
    list_per_page = 10
    
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'email', 'register_at',)
    search_fields = ('event',)
    list_filter = ('event',)
    list_per_page = 10

    

