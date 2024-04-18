import pytest

from ..tasks import (
    buy_car_between_autosalon_and_supplier,
    buy_car_between_customer_and_autosalon,
    check_deals_between_autosalons_and_suppliers,
)


@pytest.mark.django_db
def test_buy_car_between_autosalon_and_supplier(autosalon_object, supplier_object):
    """
    Test for check work first Celery task
    :param autosalon_object:
    :param supplier_object:
    :return:
    """
    assert buy_car_between_autosalon_and_supplier.create_task.run(
        autosalon_object.id, supplier_object.id
    )


@pytest.mark.django_db
def test_buy_car_between_customer_and_autosalon(
    autosalon_object, customer_object, car_object
):
    """
    Test for check work second Celery task
    :param autosalon_object:
    :param customer_object:
    :param car_object:
    :return:
    """
    assert buy_car_between_customer_and_autosalon(
        autosalon_object.id, customer_object.id, 15000, car_object
    )


@pytest.mark.django_db
def test_check_deals_between_autosalons_and_suppliers():
    """
    Test for check work third Celery task
    :return:
    """
    assert check_deals_between_autosalons_and_suppliers()
