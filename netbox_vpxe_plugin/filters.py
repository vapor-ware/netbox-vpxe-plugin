import django_filters
from django.db.models import Q

from utilities.filters import NameSlugSearchFilterSet

from .models import (
    BootProfile,
    BootImage,
    BootConfig,
)


class BootProfileFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = BootProfile
        fields = [
            'name',
            'config',
            'image',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(name__icontains=value)
            | Q(config__name__icontains=value)
            | Q(image__name__icontains=value)
        )

        return queryset.filter(qs_filter)


class BootConfigFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = BootConfig
        fields = [
            'name',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(name__icontains=value)
        )

        return queryset.filter(qs_filter)


class BootImageFilter(NameSlugSearchFilterSet):
    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )

    class Meta:
        model = BootImage
        fields = [
            'url',
            'family',
        ]

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset

        qs_filter = (
            Q(name__icontains=value) |
            Q(url__icontains=value) |
            Q(family__icontains=value)
        )

        return queryset.filter(qs_filter)
