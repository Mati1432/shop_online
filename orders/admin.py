"""Admin files."""

# Django
from django.contrib import admin

# 3rd-party
from orders.models import Order
from orders.models import OrderItem


class OrderItemInline(admin.TabularInline):  # noqa D101
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):  # noqa D101
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
