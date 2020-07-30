from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from laptops.models import Laptop
"""
  This handles GET HTTP request to http://localhost:8080/bag/
  or http://zekondi.herokuapp.com/bag

  It returns to the client html page with bag contents
  
"""

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


"""
  This handles POST HTTP request to http://localhost:8080/bag/
  or http://zekondi.herokuapp.com/bag

  It adds new item and its quantity to the shopping bag
   
"""
def add_to_bag(request, item_id):
    """ Add a quantity of the specified item to the shopping bag """

    # Get laptop of given item id
    laptop = get_object_or_404(Laptop, pk=item_id)

    # Get quantity from the request
    quantity = int(request.POST.get('quantity'))

    # Get the url to redirect to at the end
    redirect_url = request.POST.get('redirect_url')

    # Get the current bag contents from session
    bag = request.session.get('bag', {})

    # If bag has this laptop,just add new quantity to existing quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
         request,
         f'Updated quantity by {quantity} to your bag')
    
    # If bag does not have this laptop,add item as new item and its quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {laptop.name} to your bag')
    
    # Update session bag 
    request.session['bag'] = bag

    # Go to the redirect url
    return redirect(redirect_url)

"""
  This handles POST HTTP request to

  http://localhost:8080/bag/bag/djust/<item_id>/ or 
  
  http://zekondi.herokuapp.com/bag/adjust/<item_id>/

  It adjust the quantity of an item in the shopping bag
   
"""

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified item to the specified amount"""
    
    # Get the laptop information from database
    laptop = get_object_or_404(Laptop, pk=item_id)
    
    # Get quantity from request
    quantity = int(request.POST.get('quantity'))
    
    # Get the bag content from request session
    bag = request.session.get('bag', {})
    
    # Adjust the quantity if new quantity is greater than zero
    if quantity > 0:

        # Adjust item quantity to the new quantity
        bag[item_id] = quantity
        messages.success(
            request,
            f'Updated {laptop.name} quantity to  {bag[item_id]} units')
   
    # If new quantity is zero or less than zero
    else:

        # Remove item from the bag
        bag.pop(item_id)
        messages.success(request, f'Removed {laptop.name} from your bag')

    # Update session bag with the updated bag
    request.session['bag'] = bag

    # redirect to another url
    return redirect(reverse('view_bag'))

"""
  This handles POST HTTP request to
  
  http://localhost:8080/bag/bag/remove/<item_id>/ or 
  
  http://zekondi.herokuapp.com/bag/remove/<item_id>/

  It removes an item and its quantity from the shopping bag
   
"""
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:

        # Get the laptop with that id
        laptop = get_object_or_404(Laptop, pk=item_id)

        # Get bag from request session
        bag = request.session.get('bag', {})
        
        # Remove the item from bag
        bag.pop(item_id)

        # Update bag
        request.session['bag'] = bag
        messages.success(request, f'Removed {laptop.name} from your bag')
                
        return HttpResponse(status=200)
    
    # If the operation was not successful
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)