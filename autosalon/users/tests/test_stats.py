import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_customer_stats_list():
    client = APIClient()
    response = client.get(path=reverse(viewname="customer_stats-list"))
    assert response.status_code == status.HTTP_200_OK
    assert "admin_count" in response.data
    assert "manager_count" in response.data
    assert "customer_count" in response.data
    assert "email_count" in response.data
    assert "total_balance" in response.data
    assert "autosalons_count" in response.data
