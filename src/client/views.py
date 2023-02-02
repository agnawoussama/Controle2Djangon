from datetime import date
import datetime

from django.shortcuts import render
from client.models import Client
from django import forms

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'home.html', context)

def client_view(request):
    clients = Client.objects.all()
    context = {
        "clients": clients
    }
    return render(request, 'LesClient.html', context)

def client_view_10(request):
    clients = Client.objects.all()
    context = {
        "clients": clients
    }
    return render(request, 'LesClient10.html', context)

def client_view_after_2020(request):
    filteredClients = Client.objects.filter(dateEnrg__gte = '2020-05-09')    
    context = {
        "filteredClients": filteredClients
    }
    return render(request, 'LesClientAfter2020.html', context)

