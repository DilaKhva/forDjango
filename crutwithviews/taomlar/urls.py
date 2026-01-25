from django.urls import path
from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='indexmeal'),
    path('detail/<int:pk>', DetailView.as_view(), name='detailmeal'),
    path('create/', CreateMeal.as_view(), name='createmeal'),
    path('update/<int:pk>', UpdateMeal.as_view(), name='updatemeal'),
    path('delete/<int:pk>', DeleteMeal.as_view(), name='deletemeal'),
]