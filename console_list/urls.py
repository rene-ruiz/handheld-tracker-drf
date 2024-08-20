from django.urls import include, path
from rest_framework import routers

from console_list.api.viewsets import ConsoleItemViewSet, UserConsoleViewSet

router = routers.DefaultRouter()
router.register("console-items", ConsoleItemViewSet, basename="console-items")
router.register("user-consoles", UserConsoleViewSet, basename="user-console")

urlpatterns = [
    path("api/", include(router.urls)),
]
