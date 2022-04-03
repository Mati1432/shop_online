"""Views files."""
# Django
from django.shortcuts import render

# Project
from cart.cart import Cart

# Local
from .forms import OrderForm
from .models import OrderItem


def order_create(request):  # noqa D103
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            return render(request,
                          'order_finish.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request,
                  'orders_created.html',
                  {'cart': cart, 'form': form})
