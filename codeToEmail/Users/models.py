from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

class EmailCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_activated = models.BooleanField(default=False)
    expires_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=2)
        super().save(*args, **kwargs)