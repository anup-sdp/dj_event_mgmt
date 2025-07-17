# users, models.py:
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField  # for image save in cloud

class CustomUser(AbstractUser):
    #profile_image = models.ImageField(upload_to='profile_images',null=True, blank=True,  default="profile_images/default_img.png")
    profile_image  = CloudinaryField('image', folder='profile_images', blank=True, null=True, default='profile_images/default_img.png')  # to save image in cloud    
    bio = models.TextField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.pk:  # only for new users
            self.is_active = False  # set True by activation email.
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

