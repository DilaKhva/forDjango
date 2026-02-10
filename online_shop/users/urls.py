from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/<int:user_id>/', views.verify_email, name='verify_email'),
    path('', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
]