# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'address', 'city', 'state', 'zipcode', 'day', 'month', 'year', 'social_number', 'phone_number')
    
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )
    
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )
    
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )
    
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    address = forms.CharField(
        label="Address",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    city = forms.CharField(
        label="City",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    state = forms.CharField(
        label="State",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    zipcode = forms.CharField(
        label="Zip Code",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    day = forms.CharField(
        label="Day",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    month = forms.CharField(
        label="Month",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    year = forms.CharField(
        label="Year",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    social_number = forms.CharField(
        label="Social Number",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )

    phone_number = forms.CharField(
        label="Phone Number",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )



class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
    
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )
    
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'border p-2 rounded w-full outline-none focus:border-pink-500 focus:shadow-md'}),
    )