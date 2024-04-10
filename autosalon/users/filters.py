from .models import Customer, SaleHistoryOfCustomer

from django_filters import FilterSet, CharFilter, NumberFilter


class CustomerFilter(FilterSet):
    """
    Filter for CustomerViewSet
    """

    first_name = CharFilter(
        field_name="first_name", lookup_expr="exact", label="First name of Customer"
    )
    last_name = CharFilter(
        field_name="last_name", lookup_expr="exact", label="Last name of Customer"
    )
    email = CharFilter(
        field_name="email", lookup_expr="icontains", label="Email of Customer"
    )
    balance = NumberFilter(
        field_name="balance", lookup_expr="exact", label="Balance of Customer"
    )

    class Meta:
        model = Customer
        fields = ["username", "first_name", "last_name", "email", "balance"]


class SaleHistoryOfCustomerFilter(FilterSet):
    """
    Filter for SaleHistoryOfCustomerViewSet
    """

    customer_first_name = CharFilter(
        field_name="customer__first_name",
        lookup_expr="icontains",
        label="Customer first name",
    )
    customer_last_name = CharFilter(
        field_name="customer__last_name",
        lookup_expr="icontains",
        label="Customer last name",
    )
    car = CharFilter(
        field_name="car__model_name",
        lookup_expr="icontains",
        label="Car of sale history",
    )
    price = NumberFilter(
        field_name="price", lookup_expr="exact", label="Price of sale history"
    )
    date_min = NumberFilter(field_name="date", lookup_expr="gte", label="Min date")
    date_max = NumberFilter(field_name="date", lookup_expr="lte", label="Max date")

    class Meta:
        model = SaleHistoryOfCustomer
        fields = [
            "customer_first_name",
            "customer_last_name",
            "car",
            "price",
            "date_min",
            "date_max",
        ]
