
from django.urls import path
from .import views

urlpatterns = [
    path('', views.clients),
    path('clients/', views.clients, name='clients'),
]
