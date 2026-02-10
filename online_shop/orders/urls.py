from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('<int:order_id>/', views.order_detail, name='order_detail'),
    path('<int:order_id>/update-status/', views.update_order_status, name='update_order_status'),
    path('<int:order_id>/cancel/', views.cancel_order, name='cancel_order'),
    path('admin/orders/', views.admin_all_orders, name='admin_all_orders'),
    path('admin/<int:order_id>', views.admin_order_detail, name='admin_order_detail'),

]