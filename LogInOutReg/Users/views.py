from django.shortcuts import render
from django.views import View
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.

class ListView(View):
    def get(self, request):
        users = CustomUser.objects.all()
        # medicines = Medicine.objects.all()
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
        user.save()
        users = CustomUser.objects.all()
        return render(request, 'index.html', {'users': users})

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        users = CustomUser.objects.all()

        if user is None or not user.check_password(password):
            return render(request, 'auth/login.html', {'error': 'Invalid username and/or password.', 'users': users})
        login(request, user)
        return render(request, 'index.html', {'users': CustomUser.objects.all()})

def log_out(request):
    logout(request)
    return render(request, 'index.html', {'users': CustomUser.objects.all()})