from rest_framework.generics import CreateAPIView

from inventory.serializers.inventory import InventorySerializer


class CreateInventoryView(CreateAPIView):
    serializer_class = InventorySerializer
