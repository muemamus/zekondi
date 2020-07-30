from django.contrib import admin
from django.urls import path
from . import views
"""
    zekondi.herokuapp.com/bag/
    http://localhost:8080/bag/

    http://localhost:8080/bag/bag/djust/<item_id>/
    http://zekondi.herokuapp.com/bag/adjust/<item_id>/

    zekondi.herokuapp.com/bag/remove/<item_id>/
    http://localhost:8080/bag/remove/<item_id>/
    
"""
urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]
