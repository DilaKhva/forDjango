from django.contrib import admin

from .models import Order, Food

# Register your models here.

admin.site.register(Order)
admin.site.register(Food)