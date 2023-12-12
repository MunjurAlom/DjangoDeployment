from django.shortcuts import render
from .models import Client

def clients(request):
    client_data = Client.objects.all()
    data = {
        'client': client_data
    }
    return render(request, 'clients/clients.html', context=data)