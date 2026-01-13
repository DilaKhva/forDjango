from django.urls import path
from .views import get_age, get_name

urlpatterns = [
    path('users-name/', get_name),
    path('users-age/', get_age)
]