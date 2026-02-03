from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', ListView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('verify/', VerifyEmailView.as_view(), name='verify'),
]