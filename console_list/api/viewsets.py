from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from console_list.api.serializers import ConsoleItemSerializer, UserConsoleSerializer
from console_list.models import ConsoleItem, UserConsole

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