from django.urls import path
from django.shortcuts import render
from .views import home, components

urlpatterns = [
    
    path('', home, name="home"),
    path('components/', components, name="components")
]