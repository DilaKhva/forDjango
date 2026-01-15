from django.db import models

# Create your models here.

class Food(models.Model):
    food_name = models.CharField(max_length=50)
    price = models.IntegerField()
    desc = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=False)
    def __str__(self):
        return self.food_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    ordered_time = models.DateTimeField(auto_now_add=True)
    delivered_time = models.DateTimeField()
    def __str__(self):
        return f'Order id: {self.order_id}'