"""Tasks files."""
# Django
from django.core.mail import send_mail

# 3rd-party
from celery import shared_task

# Local
from .models import Order


@shared_task
def order_created(order_id):  # noqa D103
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    print('is work')
    return mail_sent
