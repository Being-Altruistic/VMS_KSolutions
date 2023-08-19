from django import forms
from .models import vms_records

class VehicleDataForm(forms.ModelForm):
    class Meta:
        model = vms_records
        fields = ('v_number', 'v_type','v_model','v_description')

