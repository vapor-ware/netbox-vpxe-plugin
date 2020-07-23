from rest_framework.serializers import ModelSerializer
from netbox_vpxe_plugin.models import (
    BootConfig,
    BootImage,
    BootProfile,
)


class BootConfigSerializer(ModelSerializer):

    class Meta:
        model = BootConfig
        fields = ('id', 'name', 'config')


class BootImageSerializer(ModelSerializer):

    class Meta:
        model = BootImage
        fields = ('id', 'name', 'url', 'family')


class BootProfileSerializer(ModelSerializer):

    class Meta:
        model = BootProfile
        fields = ('id', 'name', 'config', 'image')
