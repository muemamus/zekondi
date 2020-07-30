from django.urls import path
from . import views
from .webhooks import webhook

"""
    zekondi.herokuapp.com/checkout/
    http://localhost:8080/checkout/

    http://localhost:8080/checkout/checkout_success/<order_number>
    http://zekondi.herokuapp.com/checkout/checkout_success/<order_number>

    zekondi.herokuapp.com/checkout/cache_checkout_data/
    http://localhost:8080/checkout/cache_checkout_data/

    zekondi.herokuapp.com/checkout/wh/
    http://localhost:8080/checkout/wh/

"""

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),

]