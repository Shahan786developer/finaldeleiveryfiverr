from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.index, name='base'),
     path('dashbored/', views.dashbored, name='dashbored'),
     path('registration/', views.registration, name='registration'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('login/', views.login_view, name='login'),
     
    # Add more URL patterns for other views as needed
 ]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)