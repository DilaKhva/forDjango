from django.urls import path
from .views import get_total_price, get_order_list

urlpatterns = [
    path('view-list/', get_order_list),
    path('total-price/', get_total_price)
]