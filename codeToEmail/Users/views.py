from django.shortcuts import render, redirect
from django.views import View
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.utils import timezone

import random
from .models import EmailCode


# Create your views here.

class ListView(View):
    def get(self, request):
        users = CustomUser.objects.all()
        return render(request, 'index.html', {'users': users})


class RegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'auth/register.html', {'error': 'Passwords must match!'})

        if CustomUser.objects.filter(username=username).exists():
            return render(request, 'auth/register.html', {'error': 'Username already exists!'})


        user = CustomUser.objects.create(username=username, email=email)
        user.set_password(password)
        user.is_active = False
        user.save()

        code = str(random.randint(100000, 999999))
        EmailCode.objects.create(
            user=user,
            code=code
        )

        send_mail(
            'Your verification code',
            f'Your verification code is: {code}',
            None,  # Uses DEFAULT_FROM_EMAIL from settings
            [email],
            fail_silently=False,
        )

        return redirect('verify')


class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'auth/login.html', {'error': 'Invalid username and/or password.'})

        if not user.is_active:
            return render(request, 'auth/login.html', {'error': 'Please verify your email first.'})

        login(request, user)
        return redirect('index')


def log_out(request):
    logout(request)
    return redirect('index')


class VerifyEmailView(View):
    def get(self, request):
        return render(request, 'auth/verify.html')

    def post(self, request):
        code = request.POST.get('code')

        email_code = EmailCode.objects.filter(
            code=code,
            is_activated=False,
            expires_at__gt=timezone.now()
        ).first()

        if not email_code:
            return render(request, 'auth/verify.html', {'error': 'Invalid or expired code'})

        user = email_code.user
        user.is_active = True
        user.save()

        email_code.is_activated = True
        email_code.save()

        return redirect('login')