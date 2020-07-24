from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices


menu_items = (
    PluginMenuItem(
        link='plugins:netbox_vpxe_plugin:boot_profile_list',
        link_text='Boot Profiles',
        permissions=['netbox_vpxe_plugin.view_profile'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_vpxe_plugin:boot_profile_add',
                title='Add a new vPXE Boot Profile',
                icon_class='fa fa-plus',
                color=ButtonColorChoices.GREEN,
                permissions=['netbox_vpxe_plugin.add_profile']
            ),
        )
    ),
)
