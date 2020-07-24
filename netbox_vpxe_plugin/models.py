from django.db import models
from utilities.models import ChangeLoggedModel
from dcim.models import DeviceType
from .choices import OperatingSystemChoices, BootConfigTypeChoices


class BootImage(ChangeLoggedModel):
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


class BootConfig(ChangeLoggedModel):
    name = models.CharField(max_length=64)
    config = models.TextField()

    def __str__(self):
        return self.name

    type = models.CharField(
        max_length=30,
        choices=BootConfigTypeChoices,
        default=BootConfigTypeChoices.TYPE_PRESEED,
    )

    class Meta:
        verbose_name = 'Boot Config'
        verbose_name_plural = 'Boot Configs'


class BootProfile(ChangeLoggedModel):
    name = models.CharField(max_length=64)
    config = models.ForeignKey(
        to=BootConfig,
        on_delete=models.CASCADE,
    )

    image = models.ForeignKey(
        to=BootImage,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Boot Profile'
        verbose_name_plural = 'Boot Profiles'
