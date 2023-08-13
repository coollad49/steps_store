from django.shortcuts import render

from store.models import Product


def frontpage(request):
    products = Product.objects.filter(isfeatured = True)

    context = {
        'products': products
    }

    return render(request, 'home.html', context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')