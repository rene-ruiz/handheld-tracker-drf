from rest_framework import viewsets, permissions

from console_list.api.serializers import ConsoleItemSerializer
from .models import ConsoleItem

class ConsoleItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConsoleItem.objects.all()
    serializer_class = ConsoleItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
