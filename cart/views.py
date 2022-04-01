"""Views files."""
# Django
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.http import require_POST

# Project
from core.models import Product

# Local
from .cart import Cart
from .forms import CartForm


@require_POST
def cart_add(request, product_id):  # noqa D103
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):  # noqa D103
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):  # noqa D103
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartForm(initial={'quantity': item['quantity'],
                                                         'override': True})
    return render(request, 'cart_detail.html', {'cart': cart})
