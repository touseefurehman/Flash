from django.db import models


class item(models.Model):

    title = models.CharField(max_length=70)
    category = models.CharField(max_length=70)
    daily = models.IntegerField() 
    weekly = models.IntegerField() 
    monthly = models.IntegerField() 
    market_value = models.IntegerField() 
    quantity = models.IntegerField() 
    mini_rental_days = models.IntegerField() 
    location = models.TextField()
    description = models.TextField()
