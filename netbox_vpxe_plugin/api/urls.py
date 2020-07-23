from rest_framework import routers
from .views import (
    BootImageViewSet,
    BootConfigViewSet,
    BootProfileViewSet,
)


router = routers.DefaultRouter()
router.register('images', BootImageViewSet)
router.register('config', BootConfigViewSet)
router.register('profile', BootProfileViewSet)

urlpatterns = router.urls
