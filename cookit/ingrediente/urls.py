from rest_framework import routers
from .viewsets import IngredienteViewSet

router = routers.SimpleRouter()
router.register('ingrediente', IngredienteViewSet)

urlpatterns= router.urls