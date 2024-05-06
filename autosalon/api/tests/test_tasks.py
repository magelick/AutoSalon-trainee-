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
    :param customer_object:
    :param car_object:
    :return:
    """
    assert buy_car_between_autosalon_and_supplier.delay(
        autosalon_id=autosalon_object.id, supplier_id=supplier_object.id
    )


@pytest.mark.django_db
def test_buy_car_between_customer_and_autosalon(autosalon_object, customer_object):
    """
    Test for check work second Celery task
    :param autosalon_object:
    :param customer_object:
    :param car_object:
    :return:
    """
    assert buy_car_between_customer_and_autosalon.delay(
        autosalon_id=autosalon_object.id, customer_id=customer_object.id, price=10000.00
    )


@pytest.mark.django_db
def test_check_deals_between_autosalons_and_suppliers(
    autosalon_object, supplier_object, special_offer_of_supplier_object
):
    """
    Test for check work second Celery task
    :param autosalon_object:
    :param customer_object:
    :param car_object:
    :return:
    """
    autosalon_object.suppliers.set([supplier_object])
    check_deals_between_autosalons_and_suppliers(autosalon_id=autosalon_object.id)
    assert supplier_object in list(autosalon_object.suppliers.all())
