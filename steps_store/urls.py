"""
URL configuration for steps_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart.views import cart_detail
from core.views import frontpage, contact, about
from store.views import product_details, category_details

urlpatterns = [
    path('', frontpage, name='home'),
    path('cart/', cart_detail, name='cart_detail'),
    path('contact/', contact, name='contact'),
    path('about/',about, name='about'),
    path('admin/', admin.site.urls),
    path('<slug:category_slug>/<slug:slug>/', product_details, name='product-details'),
    path('<slug:slug>/', category_details, name='category-details'),
]
