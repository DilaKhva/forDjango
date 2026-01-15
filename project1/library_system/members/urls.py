from django.urls import path
from .views import get_name, get_age

urlpatterns = [
    path('member-name/', get_name),
    path('member-age/', get_age),
]