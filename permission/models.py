from django.db import models
from django.contrib.auth.models import AbstractUser,User

# Create your models here.
class User(AbstractUser):
    choice = (
        ('Admin', 'Admin'),
        ('Event Staff', 'Event Staff')
    )
    
    role = models.CharField( max_length=50, choices=choice, default='Admin')
    
    name = models.CharField( max_length=50)
    
    REQUIRED_FIELDS = [
        'role',
        'name',
    ]