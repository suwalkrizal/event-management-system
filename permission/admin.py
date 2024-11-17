from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'role',)
    search_fields = ('username',)
    list_filter = ('username',)
    list_per_page = 10
    
    
