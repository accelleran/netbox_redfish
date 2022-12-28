import django_tables2 as tables

from utilities.tables import BaseTable, ToggleColumn

from .models import Redfish


class RedfishTable(BaseTable):

    pk = ToggleColumn()
    device = tables.LinkColumn()
    ip = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Redfish
        fields = (
            "pk",
            "device",
            "ip",
            "power_usage",
            "power_state",
            "health_ok",
            "temp_cpu",
            "temp_mb",
        )


class RedfishBulkTable(BaseTable):

    device_type = tables.LinkColumn()

    class Meta(BaseTable.Meta):
        model = Redfish
        fields = (
            "pk",
            "device",
            "ip",
            "power_usage",
            "power_state",
            "health_ok",
            "temp_cpu",
            "temp_mb",
        )