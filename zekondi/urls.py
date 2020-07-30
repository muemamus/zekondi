from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
 Create all urls for:

 1.Home
 zekondi.herokuapp.com

 2.Admin
 zekondi.herokuapp.com/admin

 3.Accounts
 zekondi.herokuapp.com/accounts

 4.Bag
 zekondi.herokuapp.com/bag

 5.Laptops
 zekondi.herokuapp.com/laptops

 6.Checkout
 zekondi.herokuapp.com/checkout

 7.Profile
 zekondi.herokuapp.com/profile

"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('bag/', include('bag.urls')),
    path('laptops/', include('laptops.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)