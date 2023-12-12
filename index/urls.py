
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about, name='about'),
    path('our-team/', views.ourteam, name='team'),
    path('testimonials/', views.testimonials, name='testimonial'),
]
