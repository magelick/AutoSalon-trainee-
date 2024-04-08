from .models import (
    AutoSalon,
    Car,
    OptionCar,
    Supplier,
    SaleHistory,
    SpecialOfferOfAutoSalon,
    SpecialOfferOfSupplier,
)

from django_filters import (
    FilterSet,
    CharFilter,
    NumberFilter,
    BooleanFilter,
    ModelMultipleChoiceFilter,
    DateTimeFilter,
    DateTimeFromToRangeFilter
)


class AutoSalonFilter(FilterSet):
    """
    Filter for AutoSalonViewSet
    """

    name = CharFilter(
        field_name="name", lookup_expr="icontains", label="Name of Autosalon"
    )
    balance = NumberFilter(
        field_name="balance", lookup_expr="exact", label="Balance of Autosalon"
    )
    is_active = BooleanFilter(field_name="is_active", label="Is active")
    suppliers = ModelMultipleChoiceFilter(
        queryset=Supplier.objects.get_queryset(),
        field_name="suppliers",
        label="Suppliers of Autosalon",
    )
    customers = ModelMultipleChoiceFilter(
        queryset=Supplier.objects.all(),
        field_name="customers",
        label="Customers of Autosalon",
    )

    class Meta:
        model = AutoSalon
        fields = ["name", "location", "balance", "suppliers", "customers", "is_active"]


class CarFilter(FilterSet):
    """
    Filter for CarViewSet
    """
    model_name = CharFilter(field_name="model_name", lookup_expr="icontains", label="Model of Car")
    autosalons = ModelMultipleChoiceFilter(queryset=AutoSalon.objects.get_queryset(), field_name="autosalons", label="Autosalon with this car")
    options = ModelMultipleChoiceFilter(queryset=OptionCar.objects.get_queryset(), field_name="options", label="Options in this car")
    is_active = BooleanFilter(field_name="is_active", label="Is active")

    class Meta:
        model = Car
        fields = ["model_name", "autosalons", "options", "is_active"]


class OptionCarFilter(FilterSet):
    """
    Filter for OptionCarViewSet
    """

    year = DateTimeFilter(field_name="year", lookup_expr="year", label="Year of car")
    year_range = DateTimeFromToRangeFilter(field_name="year", lookup_expr="year", label="Range year of car")
    mileage_min = NumberFilter(field_name="mileage", lookup_expr="gte", label="Min mileage")
    mileage_max = NumberFilter(field_name="mileage", lookup_expr="lte", label="Max mileage")
    cars = ModelMultipleChoiceFilter(queryset=Car.objects.get_queryset(), field_name="cars", label="Cars with this options")

    class Meta:
        model = OptionCar
        fields = ["year", "year_range", "mileage_min", "mileage_max", "body_type", "transmission_type", "drive_unit_type", "color", "engine_type"]


class SupplierFilter(FilterSet):
    """
    Filter for SupplierViewSet
    """

    name = CharFilter(field_name="name", lookup_expr="icontains", label="Supplier name")
    year_of_issue = DateTimeFilter(field_name="year_of_issue", lookup_expr="year", label="Year of issue")
    price = NumberFilter(field_name="price", lookup_expr="exact", label="Price of cars")
    cars = ModelMultipleChoiceFilter(queryset=Car.objects.get_queryset(), field_name="cars", label="Supplier cars")
    is_active = BooleanFilter(field_name="is_active", label="Is active")

    class Meta:
        model = Supplier
        fields = ["name", "year_of_issue", "price", "cars", "is_active"]


class SaleHistoryFilter(FilterSet):
    """
    Filter for SaleHistoryViewSet
    """

    autosalon = CharFilter(field_name="autosalon__name", lookup_expr="icontains", label="Autosalon of special offer")
    supplier = CharFilter(field_name="supplier__name", lookup_expr="icontains", label="Supplier of special offer")
    price = NumberFilter(field_name="price", lookup_expr="exact", label="Price of special offer")

    class Meta:
        model = SaleHistory
        fields = ["autosalon", "supplier", "price"]


class SpecialOfferOfAutoSalonFilter(FilterSet):
    """
    Filter for SpecialOfferOfAutoSalonViewSet
    """
    name = CharFilter(field_name="name", lookup_expr="icontains", label="Special offer name")
    discount_min = NumberFilter(field_name="discount", lookup_expr="gte", label="Min discount")
    discount_max = NumberFilter(field_name="discount", lookup_expr="lte", label="Max discount")
    dealer = CharFilter(field_name="dealer__name", lookup_expr="icontains", label="Autosalon of special offer")
    start_date = DateTimeFilter(field_name="start_date", label="First day fo special offer")
    end_date = DateTimeFilter(field_name="end_date", label="Last day fo special offer")
    is_active = BooleanFilter(field_name="is_active", label="Is active")

    class Meta:
        model = SpecialOfferOfAutoSalon
        fields = ["name", "discount_min", "discount_max", "dealer", "start_date", "end_date", "is_active"]


class SpecialOfferOfSupplierFilter(FilterSet):
    """
    Filter for SpecialOfferOfSupplierViewSet
    """
    name = CharFilter(field_name="name", lookup_expr="icontains", label="Special offer name")
    discount_min = NumberFilter(field_name="discount", lookup_expr="gte", label="Min discount")
    discount_max = NumberFilter(field_name="discount", lookup_expr="lte", label="Max discount")
    supplier = CharFilter(field_name="supplier__name", lookup_expr="icontains", label="Autosalon of special offer")
    start_date = DateTimeFilter(field_name="start_date", label="First day fo special offer")
    end_date = DateTimeFilter(field_name="end_date", label="Last day fo special offer")
    is_active = BooleanFilter(field_name="is_active", label="Is active")

    class Meta:
        model = SpecialOfferOfSupplier
        fields = ["name", "discount_min", "discount_max", "supplier", "start_date", "end_date", "is_active"]
