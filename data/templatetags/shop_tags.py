from django import template

register = template.Library()

from ..models import Product, Category, SecondCategory, ProductFilter
from django.shortcuts import get_object_or_404

@register.simple_tag
def total_products_category(category_slug=None):
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return products.count()

@register.simple_tag
def total_products_second(category_slug=None):
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(SecondCategory, slug=category_slug)
        products = products.filter(thirdcategory=category)
    return products.count()

@register.simple_tag
def total_products_search(category_slug=None):
    return category_slug.qs.count()
