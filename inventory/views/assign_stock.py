from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

from inventory.models import Inventory
from inventory.serializers.stock import StockSerializer


class AssignStockView(CreateAPIView):
    serializer_class = StockSerializer

    def post(self, request, *args, **kwargs):
        try:
            inventory = Inventory.objects.get(id=request.data['inventory'])
        except ObjectDoesNotExist:
            return Response("Not found", status=HTTP_404_NOT_FOUND)
        count = int(request.data['count'])
        if inventory.unassigned_count - count < 0:
            return Response("Not enough inventory", status=HTTP_400_BAD_REQUEST)
        return super().post(request, *args, **kwargs)
