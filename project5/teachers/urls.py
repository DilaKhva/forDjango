from django.urls import path
from .views import *

urlpatterns = [
    path('teacher_name/', get_name),
    path('subject/', subject)
]