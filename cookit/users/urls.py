from rest_framework import routers
from .viewsets import UsersViewSet

router = routers.SimpleRouter()
router.register('users', UsersViewSet)

urlpatterns= router.urls