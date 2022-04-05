"""Admin files."""
# Django
from django.contrib import admin

# Local
from .models import Category, SettingsMail, Mail
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


@admin.register(SettingsMail)
class SettingsMailAdmin(admin.ModelAdmin):  # noqa D101
    list_display = ['title', 'content', 'name_campaign', 'api_key', 'name_group']
    list_filter = ['title', 'name_campaign']
    list_display_links = ('title',)
    list_editable = ['content', 'name_campaign', 'name_group']


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):  # noqa D101
    list_display = ['email']