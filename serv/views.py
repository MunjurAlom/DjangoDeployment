from django.shortcuts import render
from django.http import HttpResponse


def serv(request):
    return render(request, 'serv/services.html')

def services(request):
    return render(request, 'serv/services.html')