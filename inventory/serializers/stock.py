from rest_framework import serializers
from inventory.models import Stock


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        count = validated_data['count']
        inventory = validated_data['inventory']
        inventory.unassigned_count -= count
        inventory.save()
        return super().create(validated_data)
