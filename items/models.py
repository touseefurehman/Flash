from django.db import models


class RentalItem(models.Model):
    title = models.CharField(max_length=100)
    daily_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weekly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    monthly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    rental_period = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    market_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title
