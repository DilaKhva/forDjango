from django.urls import path
from .views import get_carname, get_price

urlpatterns = [
    path('get-name/', get_carname),
    path('get-price/', get_price)
]