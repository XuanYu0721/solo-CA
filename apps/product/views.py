from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from django.db.models import Q
from django.db.models import Count
from product.models import ProductBrand, ProductCategory, Product

# Create your views here.

# apps/product/views.py
def add_to_product(request):
    return HttpResponse("Item added to product")

def remove_from_product(request):
    return HttpResponse("Item removed from product")

def home(request):
    return render(request, 'product/search.html')

def search_view(request):
    return render(request, 'product/search.html')

def load_brands():
    with open('ecommerce_data/product_brands.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ProductBrand.objects.get_or_create(name=row['brand_name'])

def load_categories():
    with open('ecommerce_data/product_categories.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ProductCategory.objects.get_or_create(name=row['category_name'])

def search_in_csv(name, ingredients, price, brand, category):
    results = []
    with open('ecommerce_data/product.csv', 'r', encoding='latin-1') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if (not name or row['product_name'] == name) and \
               (not ingredients or row['ingredients'] == ingredients) and \
               (not price or row['price'] == price) and \
               (not brand or row['brand_name'] == brand) and \
               (not category or row['category_name'] == category):
                results.append(row)
    return results

def search_results(request):
    keywords = request.GET.get('keywords', '').strip()

    if not keywords:
        results = Product.objects.none()
    else:
        product_ids = Product.objects.filter(
            Q(name__iexact=keywords) |
            Q(ingredient__iexact=keywords) |
            Q(brand__name__iexact=keywords) |
            Q(category__name__iexact=keywords)
        ).values_list('id', flat=True).distinct()

        results = Product.objects.filter(id__in=product_ids)
    
    return render(request, 'product/search_results.html', {'results': results})


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def custom_500(request):
    return render(request, '500.html', status=500)


