from django.core.exceptions import ObjectDoesNotExist
from extras.plugins import PluginTemplateExtension


class DeviceStatus(PluginTemplateExtension):
    model = "dcim.device"

    def left_page(self):
        device = self.context["object"]
        template_filename = "netbox_redfish/device_redfish.html"

        try:
            return self.render(
                template_filename, extra_context={}
            )
        except ObjectDoesNotExist:
            return ""


template_extensions = [DeviceStatus]