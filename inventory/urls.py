from django.urls import path

from inventory.views.create_inventory import CreateInventoryView
from inventory.views.assign_stock import AssignStockView
from inventory.views.delete_inventory import DeleteInventoryView
from inventory.views.edit_inventory import EditInventoryView
from inventory.views.list_inventory import ListInventoryView

app_name = 'inventory'

urlpatterns = [
    path('list/', ListInventoryView.as_view(), name='list-inventory'),
    path('create-item/', CreateInventoryView.as_view(), name='create-item'),
    path('delete-item/<int:pk>/', DeleteInventoryView.as_view(), name='delete-item'),
    path('edit-item/<int:pk>/', EditInventoryView.as_view(), name='edit-item'),
    path('assign-stock/', AssignStockView.as_view(), name='assign-stock'),
]
