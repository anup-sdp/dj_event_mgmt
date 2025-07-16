# users, models.py:
from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField  # for image save in cloud

class CustomUser(AbstractUser):
    #profile_image = models.ImageField(upload_to='profile_images',null=True, blank=True)
    profile_image  = CloudinaryField('image', folder='profile_images', blank=True, null=True)  # image saved in cloud
    bio = models.TextField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.pk:  # only for new users
            self.is_active = False  # set True by activation email.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username