"""Views files."""
# Django
from django.shortcuts import get_object_or_404
from django.shortcuts import render

# Project
from cart.forms import CartForm
from core.forms import MailForm
from core.models import Category
from core.models import Product


def product_list(request, category_slug=None):  # noqa D103
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_detail(request, id, slug):  # noqa D103
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True,
    )
    cart_product = CartForm()
    return render(request, 'detail_product.html',
                  {'product': product, 'cart_product': cart_product})


class MailView(CreateView):  # noqa D101
    form_class = MailForm
    template_name = 'mail.html'
    success_url = '/'

    def form_valid(self, form): # noqa D102
        self.form = form

        return super().form_valid(form)
