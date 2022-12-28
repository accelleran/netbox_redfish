from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import View

from netbox.views.generic import BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView

from .filters import RedfishFilter
from .forms import RedfishForm, RedfishFilterForm
from .models import Redfish
from .tables import RedfishTable


class RedfishListView(PermissionRequiredMixin, ObjectListView):
    """View for listing all Redfish items"""
    permission_required = "netbox_redfish.view_redfish"
    queryset = Redfish.objects.all()
    filterset = RedfishFilter
    filterset_form = RedfishFilterForm
    table = RedfishTable

    template_name = "netbox_redfish/device_redfish_list.html"


class RedfishCreateView(PermissionRequiredMixin, ObjectEditView):
    """View for creating a new Redfish"""
    permission_required = "netbox_redfish.add_redfish"
    model = Redfish
    queryset = Redfish.objects.all()
    model_form = RedfishForm

    template_name = "netbox_redfish/device_redfish_edit.html"
    #default_return_url = "plugins:netbox_redfish:redfish_list"


class RedfishBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    """View for deleting one or more Redfishs."""
    permission_required = "netbox_redfish.delete_redfish"
    queryset = Redfish.objects.filter()
    table = RedfishTable
    #default_return_url = "plugins:netbox_redfish:redfish_list"


class RedfishEditView(RedfishCreateView):
    permission_required = "netbox_redfish.change_redfish"
