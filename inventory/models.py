from django.db import models
from django.db.models import CASCADE


class Inventory(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    total_count = models.PositiveIntegerField(null=False, default=0)
    unassigned_count = models.PositiveIntegerField(null=False, default=0)

    def __str__(self):
        return self.name


class Stock(models.Model):
    count = models.PositiveIntegerField(null=False, default=0)
    warehouse = models.ForeignKey("warehouses.Warehouse", on_delete=CASCADE)
    inventory = models.ForeignKey("inventory.Inventory", on_delete=CASCADE)

