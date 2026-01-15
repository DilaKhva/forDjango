from django.urls import path
from .views import get_phone, get_location

urlpatterns = [
    path('location/', get_location),
    path('phone/', get_phone)
]