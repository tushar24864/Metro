from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "metro.html")

def about(request):
    return render(request, "about.html")

def recharge(request):
    return render(request, "recharge.html")

def facility(request):
    return render(request, "facility.html")

def contact(request):
    return render(request, "contact.html")