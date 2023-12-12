
    # views.py
from django.shortcuts import render
from .models import PortfolioItem

def portfolio_view(request):
    portfo_data = PortfolioItem.objects.all()
    data = {
        'portfo': portfo_data
    }
    return render(request, 'portfo/portfolio.html',context=data)
