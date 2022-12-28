import django_filters
from django.db.models import Q

from dcim.models import Device
from ipam.models import IPAddress

from .models import Redfish

from netbox.filtersets import OrganizationalModelFilterSet

class RedfishFilter(OrganizationalModelFilterSet):

    q = django_filters.CharFilter(method="search", label="Search",)

    ip = django_filters.ModelMultipleChoiceFilter(
        field_name="ipaddress__slug",
        queryset=IPAddress.objects.filter.distinct(),
        to_field_name="slug",
        label="Manufacturer",
    )
    device = django_filters.ModelMultipleChoiceFilter(
        field_name="device__slug",
        queryset=Device.objects.filter.distinct(),
        to_field_name="slug",
        label="Device Type",
    )


    class Meta:
        model = Redfish
        fields = ["id","device","ip","power_usage","power_state","health_ok","temp_cpu","temp_mb"]

    def search(self, queryset, name, value):
        """Perform the filtered search."""

        if not value.strip():
            return queryset
        qs_filter = (
            Q(id__icontains=value)
            | Q(device__slug=value)
            | Q(ipaddress__slug=value)
        )
        return queryset.filter(qs_filter)