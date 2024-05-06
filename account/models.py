from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
# models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)
    location = models.CharField(max_length=255)
    profile_description = models.TextField(max_length=200) 
    profile_image = models.ImageField(upload_to='rental_item_images/', blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)

    
    def __str__(self):
        return self.user.username
