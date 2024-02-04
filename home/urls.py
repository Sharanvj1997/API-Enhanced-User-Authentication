# registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # Additional registration-related URLs can be added here
]
