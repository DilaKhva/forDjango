from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expire_date = models.DateField(blank=True, null=True)
    created_date = models.DateField()
    desc = models.TextField(blank=True, null=True)
    # type = models.CharField(max_length=100, choices=(('tech', 'Tech'),('clothes', 'Clothes'), ('food', 'Food'), ('others', 'Others')))
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    amount = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
