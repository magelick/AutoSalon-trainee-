from __future__ import absolute_import, unicode_literals

from celery import shared_task
from django.shortcuts import get_object_or_404

from .models import AutoSalon, Supplier, SaleHistory, SpecialOfferOfSupplier, Car

from users.models import Customer, SaleHistoryOfCustomer


@shared_task()
def buy_car_between_autosalon_and_supplier(autosalon_id, supplier_id):
    """
    Celery task, which make process buying car between autosalon and supplier
    :return:
    """
    # get instances
    autosalon = get_object_or_404(AutoSalon, id=autosalon_id)
    supplier = get_object_or_404(Supplier, id=supplier_id)

    # check balance of autosalon
    if autosalon.balance < supplier.price:
        raise ValueError("Autosalon doesn't has money")

    # change balance of autosalon by supplier price and add cars in autosalon
    autosalon.balance -= supplier.price
    autosalon.save()

    # add cars in autosalon
    supplier_cars = Car.objects.filter(suppliers_of_car=supplier)

    for car in supplier_cars:
        autosalon.cars.add(car)
    autosalon.save()

    # create sale history for this deal
    SaleHistory.objects.create(
        autosalon=autosalon, supplier=supplier, price=supplier.price
    )


@shared_task()
def buy_car_between_customer_and_autosalon(autosalon_id, customer_id, price):
    """
    Celery task, which make process buying car between customer and autosalon
    :return:
    """
    # get instances
    autosalon = get_object_or_404(AutoSalon, id=autosalon_id)
    customer = get_object_or_404(Customer, id=customer_id)
    car = Car.objects.filter(model_name="AUDI RS7 PERFORMANCE").first()

    # check car by exists
    if car is None:
        raise ValueError("Car not found")

    # check balance of customer
    if customer.balance < price:
        raise ValueError("Customer doesn't has money")

    # change and save balance of autosalon
    autosalon.balance += price
    autosalon.save()

    # change and save balance of customer
    customer.balance -= price
    customer.save()

    # create customer sale history for this deal
    customer_sale_history = SaleHistoryOfCustomer.objects.create(
        customer=customer, car=car, price=price
    )
    customer_sale_history.save()


@shared_task()
def check_deals_between_autosalons_and_suppliers(autosalon_id):
    """
    Celery task, which check cooperation benefit between autosalons and suppliers
    :return:
    """
    # discount_price
    discount_price = 0
    # get list of suppliers
    suppliers = [
        supplier for supplier in Supplier.objects.filter(autosalons=autosalon_id)
    ]

    # iteration by every supplier
    for supplier in suppliers:

        # check this special offer
        special_offers = SpecialOfferOfSupplier.objects.filter(
            supplier=supplier.id,
        ).first()
        # if not special offer, discount price it's usual supplier price
        if special_offers is None:
            discount_price += supplier.price

        # calculate discount price and new supplier price with that
        discount_price += supplier.price * special_offers.discount / 100
        new_supplier_price = supplier.price - discount_price

        # if new supplier price less supplier price
        if not new_supplier_price < supplier.price:
            # delete this supplier in every
            for autosalon in AutoSalon.objects.all():
                autosalon.suppliers.all().clear()
        else:
            pass
