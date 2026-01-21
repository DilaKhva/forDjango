from django.urls import path
from .views import index, detail, create_product, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>', detail, name='detail'),
    path('create/', create_product, name='create_product'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
]