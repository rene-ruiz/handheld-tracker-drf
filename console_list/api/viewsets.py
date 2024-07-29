from rest_framework.viewsets import ModelViewSet

from console_list.api.serializers import ConsoleItemSerializer
from console_list.models import ConsoleItem


class ConsoleItemViewSet(ModelViewSet):
    queryset = ConsoleItem.objects.all()
    serializer_class = ConsoleItemSerializer
