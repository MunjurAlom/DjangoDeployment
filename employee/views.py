from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def employee(request):
    return render(request, 'employee/profile.html')
@login_required
def profile(request):
    return render(request, 'employee/profile.html')