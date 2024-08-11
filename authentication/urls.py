from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from authentication.views import LogoutView, RegisterView, UserInfoView

urlpatterns = [
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/login/", TokenObtainPairView.as_view(), name="login"),
    path("api/userinfo/", UserInfoView.as_view(), name="userinfo"),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
