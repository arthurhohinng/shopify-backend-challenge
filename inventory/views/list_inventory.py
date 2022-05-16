from rest_framework.generics import ListAPIView

from inventory.models import Inventory
from inventory.serializers.inventory import InventorySerializer


class ListInventoryView(ListAPIView):
    serializer_class = InventorySerializer
    queryset = Inventory.objects.all()
