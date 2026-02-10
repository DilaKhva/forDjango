from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import render, redirect

from .models import User, EmailCode
from cart.models import Cart
from products.models import Product, Category
from datetime import timedelta
import random
from users.models import User, EmailCode



def register(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        if User.objects.filter(username=username).exists():
            error = 'Username already exists.'
        elif User.objects.filter(email=email).exists():
            error = 'Email already exists.'
        else:
            try:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    gender=gender
                )

                Cart.objects.create(user=user)

                code = f"{random.randint(100000, 999999)}"
                EmailCode.objects.create(
                    user=user,
                    code=code,
                    expire_date=timezone.now() + timedelta(minutes=2),
                    is_activated=False
                )

                send_mail(
                    'Verify your email',
                    f'Your verification code is: {code}',
                    'no-reply@shop.com',
                    [email],
                    fail_silently=False,
                )

                return redirect('verify_email', user_id=user.id)

            except Exception as e:
                error = f"Something went wrong: {str(e)}"

    return render(request, 'users/register.html', {'error': error})


def verify_email(request, user_id):
    user = get_object_or_404(User, id=user_id)
    error = None

    if EmailCode.objects.filter(user=user, is_activated=True).exists():
        login(request, user)
        return redirect('login')

    if request.method == 'POST':
        code = request.POST.get('code', '').strip()

        email_code = EmailCode.objects.filter(
            user=user,
            is_activated=False
        ).order_by('-created_at').first()


        if not email_code:
            error = 'No verification code found. Please register again.'
        elif timezone.now() > email_code.expire_date:
            error = 'Code expired. Please register again.'

        elif email_code.code != code:
            error = 'Invalid verification code. Please check and try again.'

        else:

            email_code.is_activated = True
            email_code.save()

            user.is_active = True
            user.save()

            login(request, user)
            messages.success(request, 'Email verified successfully! Welcome!')

            return redirect('login')

    return render(request, 'users/verify_email.html', {
        'error': error,
        'user': user
    })


def log_in(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, 'You are successfully logged in!')
            return redirect('products_list')
        else:
            error = 'Invalid credentials'

    return render(request, 'users/login.html', {'error': error})


def log_out(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('products_list')


def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'users/profile.html', {
        'user': request.user
    })


def update_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.gender = request.POST.get('gender')
        user.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile')

    return render(request, 'users/update_profile.html')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')

    error = None
    success = None

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        if request.user.check_password(old_password):
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, 'Password changed successfully. Please log in again.')
            return redirect('products_list')
        else:
            error = 'Wrong password'

    return render(request, 'users/change_password.html', {'error': error, 'success': success})
