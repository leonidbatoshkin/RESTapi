from rest_framework import serializers
from ..models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'description',
            'cost'
        ]

    def validate(self, data):
        description = data.get("description", None)
        if description == "":
            description = None
        cost = data.get("cost", None)
        if description is None and cost is None:
            raise serializers.ValidationError("Description or cost is required.")
        return data
