from django.urls import path

from warehouses.views.create_warehouse import CreateWarehouseView
from warehouses.views.list_items import ListItemsView

app_name = 'warehouses'

urlpatterns = [
    path('create/', CreateWarehouseView.as_view(), name='create-warehouse'),
    path('<int:pk>/', ListItemsView.as_view(), name='list-items')
]
