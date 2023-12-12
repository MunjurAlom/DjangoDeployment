from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from authentication.func import UserLogin
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        user = UserLogin(request,username=username,password=password)
        if user:
            login(request, user)
            return redirect('employee')
        if user ==None:
            messages.warning(request,"Invalid username or password")
            return redirect('login')
    return render(request, 'authentication/login.html')


def forgot_view(request):
    return render(request, 'authentication/forgot.html')

@login_required
def signout(request):
    messages.success(request,'Successfully logout')
    logout(request)
    return redirect('login')


def Signup(request):
    if request.method == 'GET':
        return render(request, 'authentication/registration.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if User.objects.filter(username=username):
            messages.warning(request,'Username is already taken')
            return render(request, 'authentication/registration.html')
        if User.objects.filter(email=email):
            messages.warning(request,'Email is already taken')
            return render(request, 'authentication/registration.html')
        if len(username) > 20 or len(username) < 5:
            messages.warning(request,'Username must be between 5 and 20 characters')
            return render(request, 'authentication/registration.html')
        if password!= confirm_password:
            messages.warning(request,'Password is not match')
            return render(request, 'authentication/registration.html')
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            messages.success(request,'Successfully create account')
            return redirect('login')
        except:
            messages.error(request,'Something went wrong')
            return render(request, 'authentication/registration.html')
        
        return render(request, 'authentication/registration.html')

