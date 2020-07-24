from django import forms

from utilities.forms import (
    BootstrapMixin,
    StaticSelect2Multiple,
)

from .models import (
    BootProfile,
    BootImage,
    BootConfig,
)

from .choices import (
    OperatingSystemChoices,
    BootConfigTypeChoices,
)

BLANK_CHOICE = (("", "---------"),)


class BootImageFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )
    family = forms.ChoiceField(
        choices=BLANK_CHOICE + OperatingSystemChoices.CHOICES,
        required=False
    )

    class Meta:
        model = BootImage
        fields = [
            'q',
            'family',
            'url',
        ]


class BootConfigFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )
    type = forms.ChoiceField(
        choices=BLANK_CHOICE + BootConfigTypeChoices.CHOICES,
        required=False
    )

    class Meta:
        model = BootConfig
        fields = [
            'q',
        ]


class BootProfileFilterForm(BootstrapMixin, forms.ModelForm):
    q = forms.CharField(
        required=False,
        label="Search",
    )
    config = forms.ModelMultipleChoiceField(
        queryset=BootConfig.objects.all(),
        required=False,
        widget=StaticSelect2Multiple,
    )
    image = forms.ModelMultipleChoiceField(
        queryset=BootImage.objects.all(),
        required=False,
        widget=StaticSelect2Multiple,
    )

    class Meta:
        model = BootProfile
        fields = [
            'q',
            'config',
            'image',
        ]
