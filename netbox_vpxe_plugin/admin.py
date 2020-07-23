from django.contrib import admin
from .models import BootImage, BootConfig, BootProfile


@admin.register(BootImage)
class BootImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'url')


@admin.register(BootConfig)
class BootConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(BootProfile)
class BootProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'config')
