from django.shortcuts import render, get_object_or_404
from .models import Laptop

# Create your views here.


def all_laptops(request):
    """ A view to return the index page """

    laptops = Laptop.objects.all()

    context = {
        'laptops': laptops,
    }
    return render(request, 'laptops/laptops.html',context)


def laptop_detail(request, laptop_id):
    """ A view to show individual laptop details """
    laptop = get_object_or_404(Laptop, pk=laptop_id)

    context = {
        'laptop': laptop,
    }
    return render(request, 'laptops/laptop_detail.html', context)