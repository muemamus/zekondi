from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from laptops.models import Laptop
from bag.contexts import bag_contents

import stripe
import json

"""
  This handles POST HTTP request to http://localhost:8080/checkout/cache_checkout_data/
  or http://zekondi.herokuapp.com/checkout/cache_checkout_data/

  It does payment processing by sending the required information to stripe
  API

"""
@require_POST
def cache_checkout_data(request):
    try:
        # Send request to stripe for payment processing
        # You need stripe API keys,user information and amount
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRETcache_checkout_data/_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)

        # Send error back if the payment processing fail
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

"""
  This handles GET HTTP request to http://localhost:8080/checkout/
  or http://zekondi.herokuapp.com/checkout

  It sends back  to the client a webpage to that collect user billing
  informaton and his/her total amount spend on laptops

  This also handles POST HTTP request to http://localhost:8080/checkout/
  or http://zekondi.herokuapp.com/checkout

"""

def checkout(request):

    # Stripe API keys required if you want to do stripe payment processing
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    # This handles POST request to this view
    if request.method == 'POST':

        # Get user bag from request session
        bag = request.session.get('bag', {})
        
        # Get form data from request
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        # Make an order form
        order_form = OrderForm(form_data)

        # Do order form validation

        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in bag.items():
                try:
                    laptop = Laptop.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                            order=order,
                            laptop=laptop,
                            quantity=item_data,
                        )
                    order_line_item.save()
                    
                except Laptop.DoesNotExist:
                    messages.error(request, (
                        "One of the laptop in your bag wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse(
                'checkout_success', 
                args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    
    
    # If the HTTP request method is not of type POST
    else:

        # Shopping bag
        bag = request.session.get('bag', {})

        # if user shopping bag is empty
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('laptops'))
        
        # If the user shopping bag is not empty

        # Know what is user bag
        current_bag = bag_contents(request)

        # Know user bag grand total
        total = current_bag['grand_total']
        stripe_total = round(total * 100)

        # Get stripe secret key
        stripe.api_key = stripe_secret_key

        # Send payment intent to stripe
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

"""
  This handles GET HTTP request to

  http://localhost:8080/checkout/checkout/checkout_success/<order_number>
  
  http://zekondi.herokuapp.com/checkout/checkout_success/<order_number>

  

"""
def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    # Get save information from request session
    save_info = request.session.get('save_info')

    # Get order using order number
    order = get_object_or_404(Order, order_number=order_number)

    # Tell user order is confirmed
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    # Delete bag content from request session
    if 'bag' in request.session:
        del request.session['bag']
    
    # Template send to the client
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    
    return render(request, template, context)