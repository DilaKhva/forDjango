from django.urls import path
from .views import *

urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('create/', CreateView.as_view(), name='create'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
]