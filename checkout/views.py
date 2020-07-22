from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('laptops'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51H7JptBFfpnxyqoyhELdq19HAlc0C8nl0tZzdBWMPXjrT7gMsNBgTDEe28TdM6cAduWzeGi2S9T9aIpgSKO9qtpJ003jLdga5G',
        'client_secret_key': 'This is a secret key'
        }

    return render(request, template, context)