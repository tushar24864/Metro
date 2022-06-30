from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
       path('', views.home, name="home"),
       path('about', views.about, name="about"),
       path('recharge', views.recharge, name="recharge"),
       path('facility', views.facility, name="facility"),
       path('contact', views.contact, name="contact"),
]