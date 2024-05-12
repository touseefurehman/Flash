from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class RentalItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2)
    weekly_price = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2)
    rental_period = models.IntegerField()
    category = models.CharField(max_length=255)
    market_value = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='rental_item_images/', blank=True, null=True)        

    
    def __str__(self):
        return self.title
