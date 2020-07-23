from rest_framework.viewsets import ModelViewSet
from netbox_vpxe_plugin.models import (
    BootImage,
    BootConfig,
    BootProfile,
)
from .serializers import (
    BootImageSerializer,
    BootConfigSerializer,
    BootProfileSerializer,
)


class BootImageViewSet(ModelViewSet):
    queryset = BootImage.objects.all()
    serializer_class = BootImageSerializer


class BootConfigViewSet(ModelViewSet):
    queryset = BootConfig.objects.all()
    serializer_class = BootConfigSerializer


class BootProfileViewSet(ModelViewSet):
    queryset = BootProfile.objects.all()
    serializer_class = BootProfileSerializer
