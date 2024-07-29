from django.urls import include, path
from rest_framework import routers

from console_list.api.viewsets import ConsoleItemViewSet

router = routers.DefaultRouter()
router.register("console-items", ConsoleItemViewSet, basename="console-items")

urlpatterns = [
    path("api/", include(router.urls)),
]
