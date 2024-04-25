import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_customer_stats_list():
    client = APIClient()
    response = client.get(path=reverse(viewname="customer_stats-list"))
    assert response.status_code == status.HTTP_200_OK
    if response.data:
        assert [
            "admin_count",
            "manager_count",
            "customer_count",
            "email_count",
            "total_balance",
            "autosalons_count",
        ] == list(response.data.keys())
