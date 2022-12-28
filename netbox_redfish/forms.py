from django import forms

from dcim.models import Device
from ipam.models import IPAddress
from utilities.forms import BootstrapMixin
from .models import Redfish

BLANK_CHOICE = (("", "---------"),)

class RedfishForm(BootstrapMixin, forms.ModelForm):

    device = forms.ModelChoiceField(
        queryset=Device.objects.distinct(),
        required=True,
        to_field_name="slug",
        label="Device",
    )

    ip = forms.ModelChoiceField(
        queryset=IPAddress.objects.distinct(),
        required=True,
        to_field_name="slug",
        label="IP",
    )


    class Meta:
        model = Redfish
        fields = ["device","ip", "username", "password"]
        obj_type = "test"

class RedfishFilterForm(BootstrapMixin, forms.ModelForm):

    device = forms.ModelChoiceField(
        queryset=Device.objects.distinct(),
        required=True,
        to_field_name="slug",
        label="Device",
    )

    ip = forms.ModelChoiceField(
        queryset=IPAddress.objects.distinct(),
        required=True,
        to_field_name="slug",
        label="IP",
    )

    q = forms.CharField(required=False, label="Search")

    class Meta:
        model = Redfish
        fields = ["device", "ip"]


