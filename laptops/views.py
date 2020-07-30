from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Laptop

"""

  This handles GET HTTP request to http://localhost:8080/laptops or 
  http://zekondi.herokuapp.com/laptops

  It sends back  to the client a list of laptops inside HTML file.

  The clients can also search the list of laptops by using either name of the laptop
  and price.

  http://zekondi.herokuapp.com/laptops?q=name
  http://zekondi.herokuapp.com/laptops?q=price
 
  The clients can also the sort list of laptops using price either in ascending
  or descending order

  http://zekondi.herokuapp.com/laptops/?sort=price&direction=asc
  http://zekondi.herokuapp.com/laptops/?sort=price&direction=desc


"""


def all_laptops(request):
    """ A view to return the index page """

    laptops = Laptop.objects.all()
    query = None
    sort = None
    direction = None
    
    # Sort the list of laptops
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                laptops = laptops.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            laptops = laptops.order_by(sortkey)

        # Search the list of laptops using name or price
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(price__icontains=query) 
            laptops = laptops.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'laptops': laptops,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'laptops/laptops.html',context)


"""
  This handles GET HTTP request to http://localhost:8080/laptops/<laptop_id>
  or http://zekondi.herokuapp.com/laptops/<laptop_id>

  It sends back  to the client information of a laptop with given laptop id
  inside HTML file.

"""

def laptop_detail(request, laptop_id):
    """ A view to show individual laptop details """
    laptop = get_object_or_404(Laptop, pk=laptop_id)

    context = {
        'laptop': laptop,
    }
    return render(request, 'laptops/laptop_detail.html', context)