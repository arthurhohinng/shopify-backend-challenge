from rest_framework.generics import CreateAPIView

from warehouses.serializers.warehouse import WarehouseSerializer


class CreateWarehouseView(CreateAPIView):
    serializer_class = WarehouseSerializer
