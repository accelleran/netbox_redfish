from django.urls import path
from . import models

from .views import (
    RedfishBulkDeleteView,
    RedfishCreateView,
    RedfishEditView,
    RedfishListView,
)
app_name = 'netbox_redfish'

urlpatterns = [
    path("redfish/", RedfishListView.as_view(), name="redfish_list", namespace='netbox_redfish'),
    path("redfish/add/", RedfishCreateView.as_view(), name="redfish_add", namespace='netbox_redfish'),
    path("redfish/delete/", RedfishBulkDeleteView.as_view(), name="redfish_bulk_delete", namespace='netbox_redfish'),
    path("redfish/<int:pk>/edit/", RedfishEditView.as_view(), name="redfish_edit", namespace='netbox_redfish'),
]