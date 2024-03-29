from django.utils.decorators import method_decorator
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.cache import cache_page

from .models import (
    AutoSalon,
    Car,
    OptionCar,
    Supplier,
    SaleHistory,
    SpecialOfferOfAutoSalon,
    SpecialOfferOfSupplier,
)

from .serializers import (
    AutoSalonSerializer,
    CarSerializer,
    OptionCarSerializer,
    SupplierSerializer,
    SaleHistorySerializer,
    SpecialOfferOfAutoSalonSerializer,
    SpecialOfferOfSupplierSerializer,
)


class ViewSetCache(ModelViewSet):
    """
    Basic ViewSet with caches
    """

    @method_decorator(cache_page(60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class AutoSalonViewSet(ViewSetCache):
    """
    ViewSet for AutoSalon model
    """

    serializer_class = AutoSalonSerializer
    queryset = AutoSalon.objects.prefetch_related("suppliers", "customers").all()


class CarViewSet(ViewSetCache):
    """
    ViewSet for Car model
    """

    serializer_class = CarSerializer
    queryset = Car.objects.prefetch_related("autosalons", "options").all()


class OptionCarViewSet(ViewSetCache):
    """
    ViewSet for OptionCar model
    """

    serializer_class = OptionCarSerializer
    queryset = OptionCar.objects.prefetch_related("cars").all()


class SupplierViewSet(ViewSetCache):
    """
    ViewSet for Supplier model
    """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.prefetch_related("cars").all()


class SaleHistoryViewSet(ViewSetCache):
    """
    ViewSet for SaleHistory model
    """

    serializer_class = SaleHistorySerializer
    queryset = SaleHistory.objects.select_related("autosalon", "supplier")


class SpecialOfferOfAutoSalonViewSet(ViewSetCache):
    """
    ViewSet for SpecialOfferOfAutoSalon model
    """

    serializer_class = SpecialOfferOfAutoSalonSerializer
    queryset = SpecialOfferOfAutoSalon.objects.select_related("dealer").all()


class SpecialOfferOfSupplierViewSet(ViewSetCache):
    """
    ViewSet for SpecialOfferOfSupplier model
    """

    serializer_class = SpecialOfferOfSupplierSerializer
    queryset = SpecialOfferOfSupplier.objects.select_related("supplier").all()
