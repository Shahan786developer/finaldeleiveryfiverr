from django.shortcuts import render

from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import *



def index(request):
    if request.user.is_authenticated:
       return render(request, 'creditapp/dd.html') 
      
    return render(request, 'creditapp/home.html')

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('base')  # Redirect to the home page after registration
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'creditapp/registration.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to the desired page after a successful login
            return redirect('base')  # Change 'home' to your desired URL name.
    else:
        form = CustomUserLoginForm()

    return render(request, 'creditapp/login.html', {'form': form})

# Import necessary modules
from django.http import JsonResponse
import requests


from django.http import JsonResponse
from django.shortcuts import render

def c(request):
        
            config = "YOUR_config_PARAMETER"
            url = "https://api-sandbox.stitchcredit.com/api/experian/credit-profile/credit-report/basic/" + config

            payload = {
            "firstName": {
                "type": "string"
            },
            "lastName": {
                "type": "string"
            },
            "street1": {
                "type": "string"
            },
            "street2": {
                "type": "string"
            },
            "city": {
                "type": "string"
            },
            "state": {
                "type": "string"
            },
            "zip": {
                "type": "string"
            },
            "ssn": {
                "type": "string"
            }
            }

            headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer <YOUR_JWT_HERE>"
            }

            response = requests.post(url, json=payload, headers=headers)

            data = response.json()
            print(data)

