
from django.urls import path
from .import views

urlpatterns = [
    path('', views.authlogin, name='login'),
    path('signup', views.Signup, name='signup'),
    path('forgot_pass', views.forgot_view, name='forgot'),
    path('logout', views.signout, name='signout'),
  
]
