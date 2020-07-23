from django.db import models
from dcim.models import DeviceType
from .choices import OperatingSystemChoices, BootConfigTypeChoices


class BootImage(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()
    family = models.CharField(
        max_length=30,
        choices=OperatingSystemChoices,
        default=OperatingSystemChoices.TYPE_OTHER,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Boot Image'
        verbose_name_plural = 'Boot Images'


class BootConfig(models.Model):
    name = models.CharField(max_length=64)
    config = models.TextField()

    type = models.CharField(
        max_length=30,
        choices=BootConfigTypeChoices,
        default=BootConfigTypeChoices.TYPE_PRESEED,
    )

    class Meta:
        verbose_name = 'Boot Config'
        verbose_name_plural = 'Boot Configs'


class BootProfile(models.Model):
    name = models.CharField(max_length=64)
    boot_config = models.ForeignKey(
        to=BootConfig,
        on_delete=models.CASCADE,
    )

    boot_image = models.ForeignKey(
        to=BootImage,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Boot Profile'
        verbose_name_plural = 'Boot Profiles'
