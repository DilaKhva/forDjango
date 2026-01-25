from django.db import models

# Create your models here.

class Meal(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    desc = models.CharField(max_length=200, blank=True, null=True)
    is_spicy = models.BooleanField(default=False)
    calories = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.title

