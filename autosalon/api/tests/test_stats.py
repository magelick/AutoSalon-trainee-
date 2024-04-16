import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_autosalon_stats_list(self):
    response = self.client.get(path=reverse(viewname="autosalon_stats"))
    assert response.status_code == status.HTTP_200_OK
    assert "suppliers_count" in response.data
    assert "cars_count" in response.data
    assert "total_price" in response.data
    assert "special_customers" in response.data
    assert "car_price" in response.data
    assert "sale_history_count" in response.data
    assert "prices_in_sale_histories" in response.data


@pytest.mark.django_db
def test_supplier_stats_list(self):
    response = self.client.get(path=reverse(viewname="supplier_stats"))
    assert response.status_code == status.HTTP_200_OK
    assert "total_prices" in response.data
    assert "autosalons_count" in response.data
    assert "cars_count" in response.data
    assert "sale_history_count" in response.data
    assert "prices_in_sale_histories" in response.data
