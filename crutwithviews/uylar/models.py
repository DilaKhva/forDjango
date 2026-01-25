from django.db import models

# Create your models here.

class Uy(models.Model):
    location = models.CharField(max_length=200)
    rooms = models.IntegerField()
    floors = models.IntegerField()
    area = models.PositiveIntegerField(help_text="Square meters")
    has_garden = models.BooleanField(default=False)
    def __str__(self):
        return f'In {self.location}'