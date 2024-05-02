from django.db import models


class item(models.Model):

    title = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    daily = models.IntegerField(max_length=20) 
    weekly = models.IntegerField(max_length=20) 
    monthly = models.IntegerField(max_length=20) 
    market_value = models.IntegerField(max_length=20) 
    quantity = models.IntegerField(max_length=20) 
    mini_rental_days = models.IntegerField(max_length=20) 
    location = models.TextField()
    description = models.TextField()