from django.utils import timezone
from datetime import timedelta

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('N', 'Prefer not to say'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


    def __str__(self):
        return self.username


class EmailCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.code} - {'Activated' if self.is_activated else 'Pending'}"

    def is_valid(self):
        return not self.is_activated and timezone.now() <= self.expire_date
