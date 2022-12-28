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
    path("redfish/", RedfishListView.as_view(), name="redfish_list"),
    path("redfish/add/", RedfishCreateView.as_view(), name="redfish_add"),
    path("redfish/delete/", RedfishBulkDeleteView.as_view(), name="redfish_bulk_delete"),
    path("redfish/<int:pk>/edit/", RedfishEditView.as_view(), name="redfish_edit"),
]