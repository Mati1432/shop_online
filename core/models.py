"""Models files."""
# Django
from django.db import models
from django.urls import reverse


class Category(models.Model):  # noqa D101
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:  # noqa D106
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):  # noqa D105
        return f'{self.name}'

    def get_absolute_url(self):  # noqa D102
        return reverse('core:product_list_by_category', args=[self.slug])


class Product(models.Model):  # noqa D101
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:  # noqa D106
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):  # noqa D105
        return f'{self.name}'

    def get_absolute_url(self):  # noqa D102
        return reverse('core:product_detail', args=[self.id, self.slug])
