from django import template


register = template.Library()

# Create a template tag to be used as a function
#  in HTML with template language
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity