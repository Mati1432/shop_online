"""Admin files."""
# Django
from django.contrib import admin

# Local
from .models import Category
from .models import Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # noqa D101
    list_display = ['name', 'slug']
    prepopulated_fields = {
        'slug': ('name',),
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):  # noqa D101
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {
        'slug': ('name',),
    }
