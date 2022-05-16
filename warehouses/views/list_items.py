from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from inventory.models import Stock
from inventory.serializers.stock import StockSerializer
from warehouses.models import Warehouse


class ListItemsView(ListAPIView):
    serializer_class = StockSerializer

    def get_queryset(self):
        try:
            requested_warehouse = Warehouse.objects.get(id=self.kwargs['pk'])
            return Stock.objects.filter(warehouse=requested_warehouse)
        except ObjectDoesNotExist:
            return []

    def get(self, request, *args, **kwargs):
        try:
            Warehouse.objects.get(id=self.kwargs['pk'])
            return super().get(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response("404 Not Found", status=HTTP_404_NOT_FOUND)
