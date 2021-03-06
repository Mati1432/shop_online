"""Urls files."""
# Django
from django.urls import path

# Local
from . import views
from .views import MailView

app_name = 'core'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('newsletter', MailView.as_view(), name='mail'),
]
