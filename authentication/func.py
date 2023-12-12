from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages


def UserLogin(request,username=None, password=None):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return user
    else:
        return None



