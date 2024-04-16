from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CustomerViewSet,
    SaleHistoryOfCustomerViewSet,
    RegisterViewSet,
    LoginViewSet,
    UpdateTokenViewSet,
    CustomerStatsViewSet,
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
# initial auth default router
auth_router = DefaultRouter()
# connect viewsets with router
auth_router.register(prefix="register", viewset=RegisterViewSet, basename="register")
auth_router.register(prefix="login", viewset=LoginViewSet, basename="login")
auth_router.register(
    prefix="update_token", viewset=UpdateTokenViewSet, basename="update_token"
)
# initial auth default router
stats_router = DefaultRouter()
# connect viewsets with router
stats_router.register(
    prefix="customer", viewset=CustomerStatsViewSet, basename="customer_stats"
)


urlpatterns = [
    path("v1/", include(router.urls)),
    path("", include(auth_router.urls)),
    path("stats/", include(stats_router.urls)),
]
