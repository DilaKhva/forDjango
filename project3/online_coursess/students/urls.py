from django.urls import path
from .views import get_name, get_age

urlpatterns = [
    path('his-name/', get_name),
    path('his-age/', get_age)
]