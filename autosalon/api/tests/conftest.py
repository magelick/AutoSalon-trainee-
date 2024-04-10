from datetime import timedelta

import pytest
from django.utils import timezone
from django_dynamic_fixture import G

from ..models import (
    AutoSalon,
    Car,
    OptionCar,
    Supplier,
    SaleHistory,
    SpecialOfferOfAutoSalon,
    SpecialOfferOfSupplier,
)

from users.models import Customer


@pytest.fixture
def customer_object():
    return G(model=Customer, first_name="Boris")


@pytest.fixture
def autosalon_object():
    return G(
        model=AutoSalon,
        name="WestCoastCustoms",
        location="US",
        balance=1000000.00,
        suppliers=[],
        customers=[],
    )


@pytest.fixture()
def car_object(autosalon_object):
    return G(model=Car, model_name="BMW M5 G30", autosalons=[], options=[])


@pytest.fixture()
def option_car_object():
    return G(
        model=OptionCar,
        year=timezone.now(),
        mileage=10000,
        body_type="sedan",
        transmission_type="automatic",
        drive_unit_type="complete",
        color="blue",
        engine_type="petrol",
        cars=[],
    )


@pytest.fixture()
def supplier_object():
    return G(
        model=Supplier,
        name="AutoHouse",
        year_of_issue=timezone.now(),
        price=50000.00,
        cars=[],
    )


@pytest.fixture()
def sale_history_object(autosalon_object, supplier_object):
    return G(
        model=SaleHistory,
        autosalon=autosalon_object.id,
        supplier=supplier_object.id,
        price=50000.00,
    )


@pytest.fixture()
def special_offer_of_autosalon_object(autosalon_object):
    return G(
        model=SpecialOfferOfAutoSalon,
        name="Sale 25%",
        descr="Special offer for customers!",
        dealer=autosalon_object.id,
        discount=25,
        start_date=timezone.now(),
        end_date=timezone.now() + timedelta(days=7),
    )


@pytest.fixture()
def special_offer_of_supplier_object(supplier_object):
    return G(
        model=SpecialOfferOfSupplier,
        name="Sale 25%",
        descr="Special offer for customers!",
        supplier=supplier_object.id,
        discount=25,
        start_date=timezone.now(),
        end_date=timezone.now() + timedelta(days=7),
    )
