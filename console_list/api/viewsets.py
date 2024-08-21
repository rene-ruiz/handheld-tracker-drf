from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from console_list.api.serializers import ConsoleItemSerializer, UserConsoleSerializer
from console_list.models import ConsoleItem, UserConsole
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ConsoleItemViewSet(ModelViewSet):
    queryset = ConsoleItem.objects.all()
    serializer_class = ConsoleItemSerializer

    def get_permissions(self):
        if self.request.method == "PATCH":
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class UserConsoleViewSet(ModelViewSet):
    serializer_class = UserConsoleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserConsole.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], url_path='console/(?P<console_item_id>[^/.]+)')
    def get_by_console_item(self, request, console_item_id=None):
        user_console = get_object_or_404(UserConsole, console_item__id=console_item_id)
        serializer = self.get_serializer(user_console)
        return Response(serializer.data)