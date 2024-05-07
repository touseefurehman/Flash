from django.db import models
from django.contrib.auth.models import User

class bio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    about = models.TextField()
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
