from django.contrib import admin
from django.urls import path
from . import views

"""
    zekondi.herokuapp.com/
    http://localhost:8080/

"""
urlpatterns = [
    path('', views.index, name='home')
]

