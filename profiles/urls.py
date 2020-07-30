from django.urls import path
from . import views

# create zekondi.herokuapp.com/profile

# create http://localhost:8080/profile

urlpatterns = [
    path('', views.profile, name='profile')
]