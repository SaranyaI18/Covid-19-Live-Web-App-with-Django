from django.contrib import admin
from django.urls import path
from .views import first

urlpatterns = [
    path('',first, name='firstpage')
]