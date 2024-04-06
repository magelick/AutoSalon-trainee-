from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CustomerViewSet,
    SaleHistoryOfCustomerViewSet,
    RegisterViewSet,
    LoginViewSet,
    UpdateTokenViewSet,
)

# initial default router
router = DefaultRouter()
# connect viewsets with router
router.register(prefix="customers", viewset=CustomerViewSet, basename="customers")
router.register(
    prefix="sale_histories",
    viewset=SaleHistoryOfCustomerViewSet,
    basename="history_customers",
)

auth_router = DefaultRouter()
auth_router.register(prefix="register", viewset=RegisterViewSet, basename="register")
auth_router.register(prefix="login", viewset=LoginViewSet, basename="login")
auth_router.register(
    prefix="update_token", viewset=UpdateTokenViewSet, basename="update_token"
)


urlpatterns = [path("v1/", include(router.urls)), path("", include(auth_router.urls))]
