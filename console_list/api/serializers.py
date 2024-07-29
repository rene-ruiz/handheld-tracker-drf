from rest_framework import serializers

from console_list.models import ConsoleItem


class ConsoleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsoleItem
        fields = [
            "id",
            "name",
            "description",
            "company",
            "image",
            "original_price",
            "obtained",
        ]
        read_only_fields = ("id",)
