from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from console_list.api.serializers import ConsoleItemSerializer
from console_list.models import ConsoleItem


class ConsoleItemViewSet(ModelViewSet):
    queryset = ConsoleItem.objects.all()
    serializer_class = ConsoleItemSerializer

    def get_permissions(self):
        if self.request.method == "PATCH":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
