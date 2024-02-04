# registration/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # Additional registration-related URLs can be added here
]
