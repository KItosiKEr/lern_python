from rest_framework import serializers
from soupsieve import select
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'title')


class BlogSerializers(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Blog
        fields = '__all__'


class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pricing
        fields = '__all__'
