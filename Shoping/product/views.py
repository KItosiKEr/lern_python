from django.shortcuts import render
from rest_framework.generics import ListAPIView
from product.models import Product
from .serializers import ProductSerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer





# Create your views here.
