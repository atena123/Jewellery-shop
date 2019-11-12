from django.shortcuts import render

# Create your views here.

def home(request):
    """A view that displays the home page"""
    return render(request, "home.html")

def info(request):
    """A view that displays the info page"""
    return render(request, "info.html")