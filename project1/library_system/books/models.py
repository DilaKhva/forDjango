from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    lang = models.CharField(max_length=20)
    price = models.IntegerField()
    pages = models.IntegerField()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name