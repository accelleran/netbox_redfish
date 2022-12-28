from django.db import models
from django.urls import reverse

from netbox.models import NetBoxModel

class Redfish(NetBoxModel):

    device = models.OneToOneField(to="dcim.Device", on_delete=models.CASCADE, blank=True, null=True)
    ip = models.OneToOneField(to="ipam.IPAddress", on_delete=models.CASCADE, blank=True, null=True)

    power_usage = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Current power usage",editable=False)
    power_state = models.CharField(blank=True, null=True, help_text="Current power state",editable=False,max_length=20,)

    health_ok = models.BooleanField(blank=True, null=True, help_text="Current health of the system",editable=False)
    temp_cpu = models.FloatField(blank=True, null=True, help_text="CPU temperature",editable=False)
    temp_mb = models.FloatField(blank=True, null=True, help_text="Motherboard temperature",editable=False)

    username = models.CharField(
        max_length=255,
        blank=True
    )

    password = models.CharField(
        max_length=255,
        blank=True
    )

    allow_power_state_change = models.BooleanField(blank=True, null=True, help_text="Allow netbox to change the power state")

    def get_power_usage(self):
        return self.power_usage

    def get_power_state(self):
        return self.power_state

    def get_health(self):
        return self.health_ok

    def get_temp_cpu(self):
        return self.temp_cpu

    def get_temp_mb(self):
        return self.temp_mb

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_allow_power_state_change(self):
        return self.allow_power_state_change

    def __str__(self):
        return f"{self.device}"

    def get_absolute_url(self):
        return reverse('plugins:netbox_redfish:redfish_list', args=[self.pk])