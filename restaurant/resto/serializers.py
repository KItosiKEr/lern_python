from rest_framework.serializers import ModelSerializer

from .models import Gellery


class GellerySerializers(ModelSerializer):
    class Meta:
        model = Gellery
        fields = '__all__'