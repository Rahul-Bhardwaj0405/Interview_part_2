from django.urls import path
from .views import HelloView, OrderView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", HelloView.as_view(), name="hello"),          #   /api/
    path("orders/", OrderView.as_view(), name="orders"),  #   /api/orders/
    path("token/", TokenObtainPairView.as_view(), name="token"),           #   /api/token/
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
