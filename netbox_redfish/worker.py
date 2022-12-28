import logging

import django_rq
from django.conf import settings

from django_rq import job

from dcim.models import Device

import coreapi
from .models import Redfish

logger = logging.getLogger("rq.worker")
logger.setLevel(logging.DEBUG)

@job
def collect_info():
    devices = Device.objects.filter().exclude(primary_ip4__isnull=True)
    logging.info("Start: Collecting Usage Information")
    results = []
    for device in devices:
        auth = coreapi.auth.BasicAuthentication(
            username=device.redfish.username,
            password=device.redfish.password
        )
        client = coreapi.Client(auth=auth)
        schema = client.get('https://' + str(device.redfish.ip) + '/redfish/v1/Systems/System.Embeded.1')
        xx = client.action(schema)

        #todo
        Redfish.objects.update_or_create(device=device, defaults={"power_usage": xx})

        data = {device.name: data}

        results.append(data)

    logging.info("FINISH: Collecting Usage Information")
    return results