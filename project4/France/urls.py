from django.urls import path

from .views import *


urlpatterns = [
    path('hi/', say_hello),
    path('city/', where_is_it),
]