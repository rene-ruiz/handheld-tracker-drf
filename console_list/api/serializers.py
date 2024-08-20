from rest_framework import serializers

from console_list.models import ConsoleItem, UserConsole


class ConsoleItemSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    class Meta:
        model = ConsoleItem
        fields = [
            "id",
            "name",
            "description",
            "company",
            "image",
            "original_price",
            "is_favorite"
        ]
        read_only_fields = ("id",)

    def get_is_favorite(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return UserConsole.objects.filter(user=user, console_item=obj).exists()
        return False

class UserConsoleSerializer(serializers.ModelSerializer):
    console_item_name = serializers.ReadOnlyField(source='console_item.name')
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserConsole
        fields = ['id', 'user', 'user_username', 'console_item', 'console_item_name', 'date_obtained']
        read_only_fields = ['id', 'user', 'date_obtained']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)