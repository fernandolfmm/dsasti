from rest_framework import routers
from .viewsets import IngredientesViewSet

router = routers.SimpleRouter()
router.register('ingredientes', IngredientesViewSet)

urlpatterns= router.urls