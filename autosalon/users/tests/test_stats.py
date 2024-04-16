import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_customer_stats_list(self):
    response = self.client.get(path=reverse(viewname="customer_stats"))
    assert response.status_code == status.HTTP_200_OK
    assert "admin_count" in response.data
    assert "manager_count" in response.data
    assert "customer_count" in response.data
    assert "email_count" in response.data
    assert "total_balance" in response.data
    assert "autosalons_count" in response.data
