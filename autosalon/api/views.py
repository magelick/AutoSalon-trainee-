from django.db.models import Count, Sum, Max, Min
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.response import Response
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


@extend_schema(tags=["Stats"])
@extend_schema_view(
    list=extend_schema(
        summary="List of AutoSalon stats",
        description="Get list of all autosalon stats",
        tags=["AutoSalon stats"],
    )
)
class AutoSalonStatsViewSet(ModelViewSet):
    """
    StatsViewSet for AutoSalon's model
    """

    serializer_class = AutoSalonSerializer

    def list(self, request, *args, **kwargs):
        # Get list autosalons with count their suppliers
        suppliers_count = AutoSalon.objects.annotate(
            suppliers_count=Count("suppliers", distinct=True)
        ).values("name", "suppliers_count")
        # Get list autosalons with count their cars
        cars_count = AutoSalon.objects.annotate(cars_count=Count("cars")).values(
            "name", "cars_count"
        )
        # Get list autosalons with their total balance
        total_price = AutoSalon.objects.annotate(total_price=Sum("balance")).values(
            "name", "total_price"
        )
        # Get list autosalons with their special cusotmers
        special_customers = AutoSalon.objects.annotate(
            special_customers=Count("customers", distinct=True)
        ).values("name", "special_customers")
        # Get list autosalons with their max and min prices
        car_price = AutoSalon.objects.annotate(
            max_price=Max("suppliers__price"), min_price=Min("suppliers__price")
        ).values("name", "max_price", "min_price")
        # Get list autosalons with their count of sale histories
        sale_history_count = AutoSalon.objects.annotate(
            sale_histories=Count("sale_history", distinct=True)
        ).values("name", "sale_histories")
        # Get list autosalons with their max and min prices in sale histories
        prices_in_sale_histories = AutoSalon.objects.annotate(
            max_price_in_history=Max("sale_history__price"),
            min_price_in_history=Min("sale_history__price"),
        ).values("name", "max_price_in_history", "min_price_in_history")
        # Define serializers
        suppliers_count_serializer = AutoSalonSerializer(
            suppliers_count, many=True
        ).data
        cars_count_serializer = AutoSalonSerializer(cars_count, many=True).data
        total_price_serializer = AutoSalonSerializer(total_price, many=True).data
        special_customers_serializer = AutoSalonSerializer(
            special_customers, many=True
        ).data
        car_price_serializer = AutoSalonSerializer(car_price, many=True).data
        sale_history_count_serializer = AutoSalonSerializer(
            sale_history_count, many=True
        ).data
        prices_in_sale_histories_serializer = AutoSalonSerializer(
            prices_in_sale_histories, many=True
        ).data
        # Define response data
        response_data = {
            "suppliers_count": suppliers_count_serializer,
            "cars_count": cars_count_serializer,
            "total_price": total_price_serializer,
            "special_customers": special_customers_serializer,
            "car_price": car_price_serializer,
            "sale_history_count": sale_history_count_serializer,
            "prices_in_sale_histories": prices_in_sale_histories_serializer,
        }
        # return Response
        return Response(response_data, status=status.HTTP_200_OK)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@extend_schema(tags=["Stats"])
@extend_schema_view(
    list=extend_schema(
        summary="List of Supplier stats",
        description="Get list of all supplier stats",
        tags=["Supplier stats"],
    )
)
class SupplierStatsViewSet(ModelViewSet):
    """
    StatsViewSet for Supplier's model
    """

    serializer_class = SupplierSerializer

    def list(self, request, *args, **kwargs):
        # Get list suppliers with their max and mib prices
        total_prices = Supplier.objects.annotate(
            max_price=Max("price"), min_price=Min("price")
        ).values("name", "max_price", "min_price")
        # Get list suppliers with count their autosalons
        autosalons_count = Supplier.objects.annotate(
            autosalons_count=Count("autosalons", distinct=True)
        ).values("name", "autosalons_count")

        # Get list suppliers with count their cars
        cars_count = Supplier.objects.annotate(
            cars_count=Count("cars", distinct=True)
        ).values("name", "cars_count")
        # Get list suppliers with count their sale histories
        sale_history_count = Supplier.objects.annotate(
            sale_histories_count=Count("sale_history", distinct=True)
        ).values("name", "sale_histories_count")
        # Get list suppliers with max and min prices in their sale histories
        prices_in_sale_histories = Supplier.objects.annotate(
            max_price_in_history=Max("sale_history__price"),
            min_price_in_history=Min("sale_history__price"),
        ).values("name", "max_price_in_history", "min_price_in_history")
        # Define serializers
        total_prices_serializer = SupplierSerializer(total_prices, many=True).data
        autosalons_count_serializer = SupplierSerializer(
            autosalons_count, many=True
        ).data
        cars_count_serializer = SupplierSerializer(cars_count, many=True).data
        sale_history_count_serializer = SupplierSerializer(
            sale_history_count, many=True
        ).data
        prices_in_sale_histories_serializer = SupplierSerializer(
            prices_in_sale_histories, many=True
        ).data
        # Define response data
        response_data = {
            "total_prices": total_prices_serializer,
            "autosalons_count": autosalons_count_serializer,
            "cars_count": cars_count_serializer,
            "sale_history_count": sale_history_count_serializer,
            "prices_in_sale_histories": prices_in_sale_histories_serializer,
        }
        # return Response
        return Response(response_data)

    @extend_schema(exclude=True)
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def partial_update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @extend_schema(exclude=True)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
