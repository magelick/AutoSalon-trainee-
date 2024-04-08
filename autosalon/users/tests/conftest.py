from datetime import timedelta

import pytest
from django.utils import timezone
from django_dynamic_fixture import G

from ..models import Customer, SaleHistoryOfCustomer

from api.models import Car

from ..filters import CustomerFilter, SaleHistoryOfCustomerFilter


@pytest.fixture()
def second_car_object():
    return G(model=Car,
             model_name="BMW M5 G30",
             autosalons=[],
             options=[])


@pytest.fixture
def customer_object():
    return G(model=Customer,
             username="admin",
             first_name="Vladimir",
             last_name="Zhirinovsky",
             email="zhirikpushka@gmail.com",
             password="russiatop!",
             balance=100000.00,
             )


@pytest.fixture
def sale_history_of_customer_object(customer_object, second_car_object):
    return G(model=SaleHistoryOfCustomer,
             customer=customer_object,
             car=second_car_object,
             price=85000.00,
             date=timezone.now(),
             )


