from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
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

from .filters import (
    AutoSalonFilter,
    CarFilter,
    OptionCarFilter,
    SupplierFilter,
    SaleHistoryFilter,
    SpecialOfferOfSupplierFilter,
    SpecialOfferOfAutoSalonFilter,
)


class ViewSetCache(ModelViewSet):
    """
    Basic ViewSet with caches
    """

    @method_decorator(cache_page(60 * 2))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


@extend_schema_view(
    list=extend_schema(
        summary="List of Autosalons",
        description="Get list of all Autosalons",
        tags=["Autosalon"],
    ),
    create=extend_schema(
        summary="New Autosalon", description="Create new Autosalon", tags=["Autosalon"]
    ),
    retrieve=extend_schema(
        summary="Get Autosalon", description="Get Autosalon by id", tags=["Autosalon"]
    ),
    update=extend_schema(
        summary="Update Autosalon",
        description="Update Autosalon by id",
        tags=["Autosalon"],
    ),
    partial_update=extend_schema(
        summary="Partial update AutoSalon",
        description="Partial update AutoSalon by id",
        tags=["Autosalon"],
    ),
    destroy=extend_schema(
        summary="Delete AutoSalon",
        description="Delete AutoSalon by id",
        tags=["Autosalon"],
    ),
)
class AutoSalonViewSet(ViewSetCache):
    """
    ViewSet for AutoSalon model
    """

    serializer_class = AutoSalonSerializer
    queryset = AutoSalon.objects.all()
    filterset_class = AutoSalonFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Cars", description="Get list of all Cars", tags=["Car"]
    ),
    create=extend_schema(summary="New Car", description="Create new Car", tags=["Car"]),
    retrieve=extend_schema(
        summary="Get Car", description="Get Car by id", tags=["Car"]
    ),
    update=extend_schema(
        summary="Update Car",
        description="Update Car by id",
        tags=["Car"],
    ),
    partial_update=extend_schema(
        summary="Partial update Car",
        description="Partial update Car by id",
        tags=["Car"],
    ),
    destroy=extend_schema(
        summary="Delete Car",
        description="Delete Car by id",
        tags=["Car"],
    ),
)
class CarViewSet(ViewSetCache):
    """
    ViewSet for Car model
    """

    serializer_class = CarSerializer
    queryset = Car.objects.all()
    filterset_class = CarFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Options Car",
        description="Get list of all Option Car",
        tags=["Option Car"],
    ),
    create=extend_schema(
        summary="New Supplier", description="Create new Option Car", tags=["Option Car"]
    ),
    retrieve=extend_schema(
        summary="Get Option Car",
        description="Get Option Car by id",
        tags=["Option Car"],
    ),
    update=extend_schema(
        summary="Update Option Car",
        description="Update Option Car by id",
        tags=["Option Car"],
    ),
    partial_update=extend_schema(
        summary="Partial update Option Car",
        description="Partial update Option Car by id",
        tags=["Option Car"],
    ),
    destroy=extend_schema(
        summary="Delete Option Car",
        description="Delete Option Car by id",
        tags=["Option Car"],
    ),
)
class OptionCarViewSet(ViewSetCache):
    """
    ViewSet for OptionCar model
    """

    serializer_class = OptionCarSerializer
    queryset = OptionCar.objects.all()
    filterset_class = OptionCarFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Suppliers",
        description="Get list of all Suppliers",
        tags=["Supplier"],
    ),
    create=extend_schema(
        summary="New Supplier", description="Create new Supplier", tags=["Supplier"]
    ),
    retrieve=extend_schema(
        summary="Get Supplier", description="Get Supplier by id", tags=["Supplier"]
    ),
    update=extend_schema(
        summary="Update Supplier",
        description="Update Supplier by id",
        tags=["Supplier"],
    ),
    partial_update=extend_schema(
        summary="Partial update Supplier",
        description="Partial update Supplier by id",
        tags=["Supplier"],
    ),
    destroy=extend_schema(
        summary="Delete Supplier",
        description="Delete Supplier by id",
        tags=["Supplier"],
    ),
)
class SupplierViewSet(ViewSetCache):
    """
    ViewSet for Supplier model
    """

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filterset_class = SupplierFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Sale Histories",
        description="Get list of all Sale Histories",
        tags=["Sale History"],
    ),
    create=extend_schema(
        summary="New Sale History",
        description="Create new Sale History",
        tags=["Sale History"],
    ),
    retrieve=extend_schema(
        summary="Get Sale History",
        description="Get Sale History by id",
        tags=["Sale History"],
    ),
    update=extend_schema(
        summary="Update Sale History",
        description="Update Sale History by id",
        tags=["Sale History"],
    ),
    partial_update=extend_schema(
        summary="Partial update Sale History",
        description="Partial update Sale History by id",
        tags=["Sale History"],
    ),
    destroy=extend_schema(
        summary="Delete Sale History",
        description="Delete Sale History by id",
        tags=["Sale History"],
    ),
)
class SaleHistoryViewSet(ViewSetCache):
    """
    ViewSet for SaleHistory model
    """

    serializer_class = SaleHistorySerializer
    queryset = SaleHistory.objects.all()
    filterset_class = SaleHistoryFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Special Offers Of AutoSalon",
        description="Get list of all Special Offers Of AutoSalon",
        tags=["Special Offer Of AutoSalon"],
    ),
    create=extend_schema(
        summary="New Special Offer Of AutoSalon",
        description="Create new Special Offer Of AutoSalon",
        tags=["Special Offer Of AutoSalon"],
    ),
    retrieve=extend_schema(
        summary="Get Special Offer Of AutoSalon",
        description="Get Special Offer Of AutoSalon by id",
        tags=["Special Offer Of AutoSalon"],
    ),
    update=extend_schema(
        summary="Update Special Offer Of AutoSalon",
        description="Update Special Offer Of AutoSalon by id",
        tags=["Special Offer Of AutoSalon"],
    ),
    partial_update=extend_schema(
        summary="Partial update Special Offer Of AutoSalon",
        description="Partial update Special Offer Of AutoSalon by id",
        tags=["Special Offer Of AutoSalon"],
    ),
    destroy=extend_schema(
        summary="Delete Special Offer Of AutoSalon",
        description="Delete Special Offer Of AutoSalon by id",
        tags=["Special Offer Of AutoSalon"],
    ),
)
class SpecialOfferOfAutoSalonViewSet(ViewSetCache):
    """
    ViewSet for SpecialOfferOfAutoSalon model
    """

    serializer_class = SpecialOfferOfAutoSalonSerializer
    queryset = SpecialOfferOfAutoSalon.objects.all()
    filterset_class = SpecialOfferOfAutoSalonFilter
    filter_backends = (DjangoFilterBackend,)


@extend_schema_view(
    list=extend_schema(
        summary="List of Special Offers Of Supplier",
        description="Get list of all Special Offers Of Supplier",
        tags=["Special Offer Of Supplier"],
    ),
    create=extend_schema(
        summary="New Special Offer Of Supplier",
        description="Create new Special Offer Of Supplier",
        tags=["Special Offer Of Supplier"],
    ),
    retrieve=extend_schema(
        summary="Get Special Offer Of Supplier",
        description="Get Special Offer Of Supplier by id",
        tags=["Special Offer Of Supplier"],
    ),
    update=extend_schema(
        summary="Update Special Offer Of Supplier",
        description="Update Special Offer Of Supplier by id",
        tags=["Special Offer Of Supplier"],
    ),
    partial_update=extend_schema(
        summary="Partial update Special Offer Of Supplier",
        description="Partial update Special Offer Of Supplier by id",
        tags=["Special Offer Of Supplier"],
    ),
    destroy=extend_schema(
        summary="Delete Special Offer Of AutoSalon",
        description="Delete Special Offer Of Supplier by id",
        tags=["Special Offer Of Supplier"],
    ),
)
class SpecialOfferOfSupplierViewSet(ViewSetCache):
    """
    ViewSet for SpecialOfferOfSupplier model
    """

    serializer_class = SpecialOfferOfSupplierSerializer
    queryset = SpecialOfferOfSupplier.objects.all()
    filterset_class = SpecialOfferOfSupplierFilter
    filter_backends = (DjangoFilterBackend,)
