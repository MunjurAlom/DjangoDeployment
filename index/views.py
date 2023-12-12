from django.shortcuts import render
from .models import About, Ourteam, Testimonials, Slider
from clients.models import Client
from portfo.models import PortfolioItem
#from .models import Client


def home(request):
    about_data = About.objects.all()[0]
    slider_data = Slider.objects.all()
    client_data = Client.objects.all()
    portfo_data = PortfolioItem.objects.all()
    team_data = Ourteam.objects.all()
    
    data = {
        'about_data': about_data,
        'slider': slider_data,
        'client': client_data,
        'portfo': portfo_data,
        'team_data': team_data
    }
    return render(request, 'index.html',context=data)

def about(request):
    about_data = About.objects.all()[0]
    team_data = Ourteam.objects.all()
    testimonials_data = Testimonials.objects.all()
    data = {
        'about_data': about_data,
        'team_data': team_data,
        'testimonials_data': testimonials_data
    }
    return render(request, 'about.html',context=data)

def ourteam (request):
    team_data = Ourteam.objects.all()
    data = {
        'team_data': team_data
    }
    return render(request, 'team.html',context=data)

def testimonials (request):
    testimonials_data = Testimonials.objects.all()
    data = {
        'testimonials_data': testimonials_data
    }
    return render(request, 'testimonials.html',context=data)

