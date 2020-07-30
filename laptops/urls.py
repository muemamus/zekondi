from django.urls import path
from . import views

"""
    zekondi.herokuapp.com/laptops
    http://localhost:8080/laptops

    zekondi.herokuapp.com/laptops/<laptop_id>
    http://localhost:8080/laptops/<laptop_id>

"""




urlpatterns = [
    path('', views.all_laptops, name='laptops'),
    path('<laptop_id>', views.laptop_detail, name='laptop_detail'),

]
