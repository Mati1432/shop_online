"""Apps files."""
# Django
from django.apps import AppConfig


class CartConfig(AppConfig):  # noqa D101
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
