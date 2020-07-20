from django.shortcuts import render
from .models import Laptop

# Create your views here.


def all_laptops(request):
    """ A view to return the index page """

    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops,
    }
    return render(request, 'laptops/laptops.html',context)