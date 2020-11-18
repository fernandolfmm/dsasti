from rest_framework import viewsets
from .models import Ingredientes
from .serializer import IngredientesSerializer


class IngredientesViewSet(viewsets.ModelViewSet):
    queryset = Ingredientes.objects.all()
    serializer_class = IngredientesSerializer