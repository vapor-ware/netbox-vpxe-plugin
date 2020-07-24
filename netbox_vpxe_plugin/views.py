from django.shortcuts import render
from utilities.views import BulkDeleteView, ObjectEditView, ObjectListView, ObjectDeleteView

from .models import (
    BootProfile,
    BootImage,
    BootConfig,
)
from .filters import (
    BootProfileFilter,
    BootImageFilter,
    BootConfigFilter,
)
from .forms import (
    BootProfileFilterForm,
    BootImageFilterForm,
    BootConfigFilterForm,
)
from .tables import BootProfileTable


class BootProfileListView(ObjectListView):
    permission_required = 'netbox_vpxe_plugin.view_boot_profile'
    queryset = BootProfile.objects.all()
    filterset = BootProfileFilter
    filterset_form = BootProfileFilterForm
    table = BootProfileTable
    template_name = 'netbox_vpxe_plugin/boot_profile_list.html'
