from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

import_icon_class = "mdi mdi-upload"

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_redfish:redfish_list',
        link_text="Redfish",
        permissions=["netbox_redfish.view_redfish"],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_redfish:redfish_add',
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["netbox_redfish.add_redfish"],
            ),
        ),
    ),
)

