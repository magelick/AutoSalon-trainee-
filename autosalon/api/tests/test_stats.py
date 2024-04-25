import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_autosalon_stats_list():
    client = APIClient()
    response = client.get(path=reverse(viewname="autosalon_stats-list"))
    assert response.status_code == status.HTTP_200_OK

    if response.data:
        assert [
            "suppliers_count",
            "cars_count",
            "total_price",
            "special_customers",
            "car_price",
            "sale_history_count",
            "prices_in_sale_histories",
        ] == list(response.data.keys())


@pytest.mark.django_db
def test_supplier_stats_list():
    client = APIClient()
    response = client.get(path=reverse(viewname="supplier_stats-list"))
    assert response.status_code == status.HTTP_200_OK

    if response.data:
        assert [
            "total_prices",
            "autosalons_count",
            "cars_count",
            "sale_history_count",
            "prices_in_sale_histories",
        ] == list(response.data.keys())
