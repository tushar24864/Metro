from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Metro Admin"
admin.site.site_title = "MetroApp's Dashboard"
admin.site.index_title = "Welcome to the portal!"

urlpatterns = [
       path('', views.home, name="home"),
       path('about', views.about, name="about"),
       path('recharge', views.recharge, name="recharge"),
       path('facility', views.facility, name="facility"),
       path('contact', views.contact, name="contact"),
       path('physical', views.physical, name="physical"),
       path('women', views.women, name="women"),
       path('security', views.security, name="security"),
       path('tour', views.tour, name="tour"),
       path('lost_item', views.lost_item, name="lost_item"),
       path('saveContact', views.saveContact, name="saveContact"),
      

]