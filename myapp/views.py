
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myapp.models import Contact_us
# Create your views here.

        
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        phone_number = request.POST.get('Phone Number')
        message = request.POST.get('Massage')

        contact = Contact_us(name=name, email=email, phone_number=phone_number, message=message)
        contact.save()
    return render(request, 'contact.html')

def cycle(request):
    return render(request, 'cycle.html')

def news(request):
    return render(request, 'news.html')
