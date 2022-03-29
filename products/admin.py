from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ display category info in admin """
    list_display = ('name', 'friendly_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ display product info in admin and order by sku """
    list_display = (
        'sku',
        'name',
        'price',
        'description',
        'rating',
    )
    ordering = ('sku',)
