from django.db import models

# Create your models here.

class Davlat(models.Model):
    title = models.CharField(max_length=100)
    # flag_img = models.ImageField(upload_to='flags')
    capital = models.CharField(max_length=100)
    area = models.IntegerField()
    independence_day_year = models.DateField()
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.title
