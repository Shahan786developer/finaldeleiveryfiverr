from django.contrib import admin
from .models import *  # Use CamelCase for model name

admin.site.register(CustomUser)
