from django.urls import path
from .views import get_course_name, get_course_price

urlpatterns = [
    path('course/', get_course_name),
    path('price/', get_course_price)
]