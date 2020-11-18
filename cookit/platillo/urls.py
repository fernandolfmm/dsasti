from rest_framework import routers
from .viewsets import PlatillosViewSet

router = routers.SimpleRouter()
router.register('platillo', PlatillosViewSet)

urlpatterns= router.urls