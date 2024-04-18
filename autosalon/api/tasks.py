from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta

from .models import AutoSalon, Supplier, SaleHistory, SpecialOfferOfSupplier

from users.models import Customer, SaleHistoryOfCustomer


@shared_task()
def buy_car_between_autosalon_and_supplier(autosalon_id, supplier_id):
    """
    Celery task, which make process buying auto between autosalon and supplier
    :return:
    """
    # get instances
    autosalon = get_object_or_404(AutoSalon, id=autosalon_id)
    supplier = get_object_or_404(Supplier, id=supplier_id)

    # check balance of autosalon
    if autosalon.balance < supplier.price:
        raise ValueError("Autosalon doesn't has money")

    # change balance of autosalon by supplier price
    autosalon.balance -= supplier.price
    autosalon.save()

    # create sale history for this deal
    sale_history = SaleHistory.objects.create(
        autosalon=autosalon, supplier=supplier, price=supplier.price
    )
    sale_history.save()


@shared_task()
def buy_car_between_customer_and_autosalon(autosalon_id, customer_id, price, car):
    """
    Celery task, which make process buying auto between customer and autosalon
    :return:
    """
    # get instances
    autosalon = get_object_or_404(AutoSalon, id=autosalon_id)
    customer = get_object_or_404(Customer, id=customer_id)
    car = autosalon.objects.cars().filter(car__model_name=car).first()

    # check balance of customer
    if customer.balance < price:
        raise ValueError("Customer doesn't has money")

    # change balance of autosalon
    autosalon.balance += price
    autosalon.save()

    # change balance of customer
    customer.balance -= price
    customer.save()

    # create sale history for this deal
    sale_history = SaleHistoryOfCustomer.objects.create(
        customer=customer, autosalon=autosalon, car=car
    )
    sale_history.save()


@shared_task()
def check_deals_between_autosalons_and_suppliers():
    """
    Celery task^ which check cooperation benefit between autosalons and suppliers
    :return:
    """
    discount_price = 0
    # get list fo suppliers
    suppliers = [suppliers for suppliers in AutoSalon.objects.suppliers()]

    # iteration by every supplier
    for supplier in suppliers:
        # check this special oofer
        special_offers = SpecialOfferOfSupplier.objects.filter(
            supplier=supplier,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        # if not special oofer, discount price it's usuall supplier price
        if special_offers is None:
            discount_price += supplier.price

        # calculate discount price
        discount_price += supplier.price * special_offers.discount / 100

        # if discount price less supplier price
        if discount_price > supplier.price:
            # delete this supplier in every
            for autosalon in AutoSalon.objects.all():
                autosalon.suppliers.supplier.clear()

        else:
            pass
