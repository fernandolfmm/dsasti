from rest_framework import viewsets
from .models import Platillo
from .serializer import PlatillosSerializer


class PlatillosViewSet(viewsets.ModelViewSet):
    queryset = Platillo.objects.all()
    serializer_class = PlatillosSerializer