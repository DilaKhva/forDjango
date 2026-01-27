from django.urls import path
from .views import *

urlpatterns = [
    path('hiSpain/', spain),
    path('city/', where_is_it)
]