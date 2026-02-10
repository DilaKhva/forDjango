from django.contrib import admin
from .models import *
import string

# Register your models here.

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)