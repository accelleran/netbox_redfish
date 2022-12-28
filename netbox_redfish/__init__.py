from extras.plugins import PluginConfig

class NetboxRedfishConfig(PluginConfig):
    name = 'netbox_redfish'
    verbose_name = 'Use netbox in combination with Redfish OOB interfaces'
    description = 'Use netbox in combination with Redfish OOB interfaces'
    version = '0.1'
    base_url = 'netbox_redfish'

config = NetboxRedfishConfig