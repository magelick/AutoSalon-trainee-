from .models import Customer, SaleHistoryOfCustomer

from django_filters import FilterSet, CharFilter, NumberFilter


class CustomerFilter(FilterSet):
    """
    Filter for CustomerViewSet
    """

    # Customer first name
    first_name = CharFilter(
        field_name="first_name", lookup_expr="exact", label="First name of Customer"
    )
    # Customer last name
    last_name = CharFilter(
        field_name="last_name", lookup_expr="exact", label="Last name of Customer"
    )
    # Customer email
    email = CharFilter(
        field_name="email", lookup_expr="icontains", label="Email of Customer"
    )
    # Customer balance
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

    # Customer first name
    customer_first_name = CharFilter(
        field_name="customer__first_name",
        lookup_expr="icontains",
        label="Customer first name",
    )
    # Customer last name
    customer_last_name = CharFilter(
        field_name="customer__last_name",
        lookup_expr="icontains",
        label="Customer last name",
    )
    # Car model name
    car = CharFilter(
        field_name="car__model_name",
        lookup_expr="icontains",
        label="Car of sale history",
    )
    # Sale History price of car
    price = NumberFilter(
        field_name="price", lookup_expr="exact", label="Price of sale history"
    )
    # Dates
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
