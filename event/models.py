from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField( max_length=50)
    description = models.CharField( max_length=50)
    location = models.CharField( max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField()

    def __str__(self):
        return f"{self.title}"
    

class Participant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    register_at = models.DateTimeField()
    
    
    def __str__(self):
        return f"{self.event}-{self.name}"
    

