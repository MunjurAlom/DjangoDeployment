
from django.urls import path
from .import views

urlpatterns = [
    path('', views.serv),
    path('services/', views.services, name='serv'),
]
