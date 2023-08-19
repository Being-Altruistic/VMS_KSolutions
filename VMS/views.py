from typing import Dict
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import vms_records
from .forms import VehicleDataForm
from .utils import is_super_admin, is_admin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin



# List All the Vehicle Data | ListView
class VehicleListView(LoginRequiredMixin, ListView):
    model = vms_records
    template_name = 'home.html'
    context_object_name = "list_obj"

    def get_context_data(self, **kwargs):
        context = super(VehicleListView, self).get_context_data(**kwargs)
        context.update({
            'l1_type': self.request.user.is_superuser,
            'l2_type': self.request.user.groups.filter(name='Admin').exists(),
        })
        return context


# Create Vehicle Data | CreateView
class VehicleDataCreateView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = vms_records
    form_class = VehicleDataForm
    template_name ="create_vehicle.html"
    success_url = '/home'

    def test_func(self):
        user = self.request.user
        return is_super_admin(user)
    
    def handle_no_permission(self):
        return redirect("vms:vehicle-list")
    
    def get_success_message(self, cleaned_data):
        return f"Entry for Vehicle No.{cleaned_data['v_number']} created Successfully"




# Update Vehicle Data | UpdateView
class VehicleDataUpdateView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = vms_records
    form_class = VehicleDataForm
    template_name = "update_vehicle.html"
    success_url = '/home'

    def test_func(self):
        user = self.request.user
        return is_super_admin(user) or is_admin(user)

    def handle_no_permission(self):
        return redirect("vms:vehicle-list")

    def get_success_message(self, cleaned_data):
        return f"Entry Updated for Vehicle No.{cleaned_data['v_number']}"




# Delete Vehicle Data | DeleteView
class VehicleDataDeleteView(UserPassesTestMixin, LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = vms_records
    template_name ="confirm.html"
    success_url = '/home'


    def test_func(self):
        user = self.request.user
        return is_super_admin(user)

    def handle_no_permission(self):        
        return redirect("vms:vehicle-list")

    def get_success_message(self, cleaned_data):
        return f"Entry Deleted Successfully"
