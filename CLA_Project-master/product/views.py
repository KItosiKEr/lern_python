from django.shortcuts import render, redirect
from .models import Product

def product(request):
    context = {
        'product' : Product.objects.all()[:9]
    }
    return render(request, 'product/product.html', context)

# Create your views here.
