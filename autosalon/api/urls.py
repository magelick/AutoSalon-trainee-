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
)

# initial default router
router = DefaultRouter()
# connect viewsets with router
router.register(prefix="autosalons", viewset=AutoSalonViewSet)
router.register(prefix="cars", viewset=CarViewSet)
router.register(prefix="options_car", viewset=OptionCarViewSet)
router.register(prefix="suppliers", viewset=SupplierViewSet)
router.register(prefix="sale_histories", viewset=SaleHistoryViewSet)
router.register(
    prefix="special_offers_of_autosalon", viewset=SpecialOfferOfAutoSalonViewSet
)
router.register(
    prefix="special_offers_of_supplier", viewset=SpecialOfferOfSupplierViewSet
)

urlpatterns = [path("v1/", include(router.urls))]
