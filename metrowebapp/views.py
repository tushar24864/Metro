from django.shortcuts import render, redirect
from django.http import HttpResponse
from metrowebapp.models import contactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
        instance = contactForm(name=name, email=email, phone=phone, message=message)
        instance.save()
        return render(request, "contact.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name

        myuser.save()

        messages.success(request, "Your account has been successfully created.")

        return redirect('signin')
    return render(request, "signup.html")
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            name = user.username
            return render(request, "signedin.html", {'name':name})
        
        else:
            messages.error(request, "Invalid User")
            return redirect('home')
    return render(request, "signin.html")

