
from django.urls import path
from .import views

urlpatterns = [
    path('', views.portfolio_view),
    path('portfolio/', views.portfolio_view, name='portfo'),
]
