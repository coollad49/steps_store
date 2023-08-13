from django.shortcuts import render, get_object_or_404

from .models import Product,Category

def product_details(request, category_slug, slug):
    products = get_object_or_404(Product, slug=slug)

    context ={
        'product': products
    }

    return render(request, 'product_detail.html', context)

def category_details(request, slug):
    categories = get_object_or_404(Category, slug=slug)
    products = categories.products.all()

    context = {
        'category': categories,

        'products': products
    }

    return render(request, 'category_detail.html', context)