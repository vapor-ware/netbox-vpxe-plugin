import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import (
    BaseTable,
    ToggleColumn,
)

from .models import (
    BootProfile,
    BootImage,
    BootConfig,
)


class BootProfileTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(
        viewname='plugins:netbox_vpxe_plugin:boot_profile',
        args=[Accessor('pk')]
    )

    class Meta(BaseTable.Meta):
        model = BootProfile
        fields = (
            'pk',
            'name',
            'image',
            'config',
            'last_updated'
        )
