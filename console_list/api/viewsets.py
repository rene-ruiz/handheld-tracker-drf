from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from console_list.api.serializers import ConsoleItemSerializer, UserConsoleSerializer
from console_list.models import ConsoleItem, UserConsole
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED


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

    def create(self, request, *args, **kwargs):
        user = request.user
        console_item_id = request.data.get('console_item')

        try:
            console_item = ConsoleItem.objects.get(id=console_item_id)
        except ConsoleItem.DoesNotExist:
            return Response({"error": "ConsoleItem not found."}, status=HTTP_404_NOT_FOUND)

        user_console = UserConsole.objects.filter(user=user, console_item=console_item).first()

        if user_console:
            user_console.delete()
            return Response({"action": "removed"}, status=HTTP_200_OK)
        else:
            UserConsole.objects.create(user=user, console_item=console_item)
            return Response({"action": "added"}, status=HTTP_201_CREATED)
