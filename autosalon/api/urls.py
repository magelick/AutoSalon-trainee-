from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AutoSalonViewSet,
    CarViewSet,
    OptionCarViewSet,
    SupplierViewSet,
    SaleHistoryViewSet,
    SpecialOfferOfSupplierViewSet,
    SpecialOfferOfAutoSalonViewSet,
    AutoSalonStatsViewSet,
    SupplierStatsViewSet,
)

# initial default router
router = DefaultRouter()
# connect viewsets with router
router.register(prefix="autosalons", viewset=AutoSalonViewSet, basename="autosalons")
router.register(prefix="cars", viewset=CarViewSet, basename="cars")
router.register(prefix="options_car", viewset=OptionCarViewSet, basename="options")
router.register(prefix="suppliers", viewset=SupplierViewSet, basename="suppliers")
router.register(
    prefix="sale_histories", viewset=SaleHistoryViewSet, basename="histories"
)
router.register(
    prefix="special_offers_of_autosalon",
    viewset=SpecialOfferOfAutoSalonViewSet,
    basename="offers_autosalon",
)
router.register(
    prefix="special_offers_of_supplier",
    viewset=SpecialOfferOfSupplierViewSet,
    basename="offers_customer",
)
# initial stats default router
stats_router = DefaultRouter()
# connect viewsets with router
stats_router.register(
    prefix="autosalon", viewset=AutoSalonStatsViewSet, basename="autosalon_stats"
)
stats_router.register(
    prefix="supplier", viewset=SupplierStatsViewSet, basename="supplier_stats"
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("stats/", include(stats_router.urls)),
]
