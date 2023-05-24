from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('', index),
    path('admin/', admin.site.urls),
]
