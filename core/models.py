from django.db import models
from django.contrib.auth.models import User

# Create your models here. 

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)  # many to one # changed event to events --------------
    participants = models.ManyToManyField(User, related_name='events', blank=True)  # M2M    
    asset = models.ImageField(upload_to='events_asset', blank=True, null=True, default="events_asset/default_img.png")  # needed for assignment 2
    
    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return self.name


"""
# replace it with User model
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    events = models.ManyToManyField(Event, related_name='participants')  # many to many

    def __str__(self):
        return self.name
"""