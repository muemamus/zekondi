from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
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
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(price__icontains=query) | Q(ram_size__icontains=query)
            laptops = laptops.filter(queries)
    context = {
        'laptop': laptop,
    }
    return render(request, 'laptops/laptop_detail.html', context)