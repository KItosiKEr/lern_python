from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from . import serializers
from . import models

class BlogViewSet(ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializers


class PricingViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Pricing.objects.all()
    serializer_class = serializers.PricingSerializer

    def create(self, request, *args, **kwargs):
        """
        this method will update permission_classes
        that Admin would only creare
        """
        self.permission_classes = [permissions.IsAdminUser]
        super(PricingViewSet, self).create()

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAdminUser]
        super(PricingViewSet, self).update()

# Create your views here.
