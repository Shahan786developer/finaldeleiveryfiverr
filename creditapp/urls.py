from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.index, name='base'),
     
     path('registration/', views.registration, name='registration'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('login/', views.login_view, name='login'),
     
    # Add more URL patterns for other views as needed
]
