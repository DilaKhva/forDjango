
from django.urls import path
from .views import get_title, get_price

urlpatterns = [
    path('get-title/', get_title),
    path('get-price/', get_price)
]