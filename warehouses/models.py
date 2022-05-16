from django.db import models


class Warehouse(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    location = models.CharField(null=False, blank=False, max_length=50)

    def __str__(self):
        return "{name} ({location})".format(name=self.name, location=self.location)
