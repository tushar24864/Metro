from django.shortcuts import render, redirect
from django.http import HttpResponse
from metrowebapp.models import contactForm
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

def physical(request):
    return render(request, "ph.html")

def women(request):
    return render(request, "women.html")

def security(request):
    return render(request, "security.html")

def tour(request):
    return render(request, "tour.html")

def lost_item(request):
    return render(request, "lost-item.html")

def saveContact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        print(name, email, phone, message)
        instance = contactForm(name=name, email=email, phone=phone, message=message)
        instance.save()
    return render(request, "contact.html")

