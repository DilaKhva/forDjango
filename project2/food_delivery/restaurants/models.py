from random import choice

from django.db import models

# Create your models here.

class Restaurant(models.Model):
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    rating = models.FloatField()
    def __str__(self):
        return f'{self.title} restaurant.'

class MenuItem(models.Model):
    item_name = models.CharField(max_length=50)
    price = models.IntegerField()
    type = models.CharField(max_length=50, choices =(
        ('fast food', 'fast food'),
        ('healthy food', 'healthy food'),
        ('milliy food', 'milliy food'))
    )
    def __str__(self):
        return f'{self.item_name}'