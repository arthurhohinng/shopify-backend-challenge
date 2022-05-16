from django.core.exceptions import ObjectDoesNotExist
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from inventory.models import Inventory
from inventory.serializers.inventory import InventorySerializer


class EditInventoryView(RetrieveUpdateAPIView):
    serializer_class = InventorySerializer

    def get_object(self):
        try:
            return Inventory.objects.get(id=self.kwargs['pk'])
        except ObjectDoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        try:
            Inventory.objects.get(id=self.kwargs['pk'])
            return super().get(request, *args, **kwargs)
        except (ObjectDoesNotExist, KeyError):
            return Response("Not found", HTTP_404_NOT_FOUND)

