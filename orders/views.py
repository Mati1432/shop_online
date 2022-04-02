"""Views files."""
from django.shortcuts import render
from cart.cart import Cart
from .models import OrderItem
from .forms import OrderForm


def order_create(request):
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
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request,
                          'orders_created.html',
                          {'order': order})
    else:
        form = OrderForm()
    return render(request,
                  'order_finish.html',
                  {'cart': cart, 'form': form})
