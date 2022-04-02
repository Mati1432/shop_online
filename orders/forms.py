"""Forms files."""

# Django
from django import forms

# 3rd-party
from orders.models import Order


class OrderForm(forms.ModelForm):  # noqa D101
    class Meta:  # noqa D106
        model = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'address',
            'postal_code',
            'city',
        ]
