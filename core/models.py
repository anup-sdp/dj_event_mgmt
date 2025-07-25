from django.db import models
#from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField  # for image save in cloud
from django.contrib.auth import get_user_model

User = get_user_model()

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
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)  # many to one # changed event to events  --------------
    participants = models.ManyToManyField(User, related_name='rsvp_events', blank=True)  # M2M    # changed events to resvp_events
    #asset = models.ImageField(upload_to='events_asset', blank=True, null=True, default="events_asset/default_img.png")  # needed for assignment 2
    # Replace ImageField with CloudinaryField
    asset = CloudinaryField('image', folder='events_midterm', blank=True, null=True, default='events_midterm/default_jb8jxq.png') # 
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