from rest_framework import serializers
from .models import Platillo


class PlatillosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platillo
        fields='__all__'