from django.shortcuts import render

from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from resto.serializers import GellerySerializers
from .models import Gellery


class GelleryView(ListAPIView):
    queryset = Gellery.objects.all()
    serializer_class = GellerySerializers


class GelleryCreateView(CreateAPIView):
    queryset = Gellery.objects.all()
    serializer_class = GellerySerializers


class GelleryUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Gellery.objects.all()
    serializer_class = GellerySerializers


class GelleryDeleteView(DestroyAPIView):
    queryset = Gellery.objects.all()
    serializer_class = GellerySerializers


# Create your views here.
