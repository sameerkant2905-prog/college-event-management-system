from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


# 🟢 INDEX
def index(request):
    return render(request, 'index.html')


# 🟢 CONTACT PAGE
def contact(request):
    return render(request, 'contact.html')


# 🟢 REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        # ✅ correct method (IMPORTANT)
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Registration successful. Please login.")
        return redirect('login')

    return render(request, 'register.html')


# 🟢 LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')


# 🟢 ADMIN LOGIN (simple version)
def adminlogin_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid admin credentials")
            return redirect('admin_login')

    return render(request, 'adminlogin.html')
