from django.db import models
from django.forms import BooleanField


# Create your models here.


class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Membership(models.Model):
    types = (
        ('basic', 'Basic'),
        ('premium', 'Premium')
    )
    membership_type = models.CharField(max_length=30, choices=types)
    is_avtive_member = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    def __str__(self):
        return f'{Member.first_name} {Member.last_name}\'s membership'