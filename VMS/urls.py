from django.urls import path
from .views import (VehicleListView, VehicleDataCreateView, VehicleDataUpdateView,
                    VehicleDataDeleteView)

app_name = 'vms'
urlpatterns = [
    path('home/', view=VehicleListView.as_view(), name='vehicle-list'),
    path('create/', view=VehicleDataCreateView.as_view(), name='vehicle-save'),
    path('vehicle/<int:pk>/update/', view=VehicleDataUpdateView.as_view(), name='vehicle-update'),
    path('vehicle/<int:pk>/delete/', view=VehicleDataDeleteView.as_view(), name='vehicle-delete'),
]
