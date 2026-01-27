from django.urls import path
from .views import *

urlpatterns = [
    path('student_name/', get_name),
    path('avg_score/', avg_score),
]