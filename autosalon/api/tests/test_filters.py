import pytest

from ..filters import (
    AutoSalonFilter,
    CarFilter,
    OptionCarFilter,
    SupplierFilter,
    SaleHistoryFilter,
    SpecialOfferOfAutoSalonFilter,
    SpecialOfferOfSupplierFilter
)


@pytest.mark.django_db
def test_autosalon_name(autosalon_object):
    data = {"name": "WestCoastCustoms"}
    filter_data = AutoSalonFilter(data=data)
    assert filter_data.qs.first().name == autosalon_object.name


@pytest.mark.django_db
def test_autosalon_location(autosalon_object):
    data = {"location": "US"}
    filter_data = AutoSalonFilter(data=data)
    assert filter_data.qs.first().location == autosalon_object.location


@pytest.mark.django_db
def test_autosalon_balance(autosalon_object):
    data = {"balance": 1000000.00}
    filter_data = AutoSalonFilter(data=data)
    assert filter_data.qs.first().balance == autosalon_object.balance


@pytest.mark.django_db
def test_autosalon_suppliers(autosalon_object, supplier_object):
    data = {"suppliers": supplier_object}
    autosalon_object.suppliers.set([supplier_object])
    filter_data = AutoSalonFilter(data=data)
    assert filter_data.qs.first().suppliers == autosalon_object.suppliers


@pytest.mark.django_db
def test_autosalon_customers(autosalon_object, customer_object):
    data = {"suppliers": customer_object}
    autosalon_object.customers.set([customer_object])
    filter_data = AutoSalonFilter(data=data)
    assert filter_data.qs.first().customers == autosalon_object.customers


@pytest.mark.django_db
def test_car_model_name(car_object):
    data = {"model_name": "BMW M5 G30"}
    filter_data = CarFilter(data=data)
    assert filter_data.qs.first().model_name == car_object.model_name


@pytest.mark.django_db
def test_car_model_autosalons(car_object, autosalon_object):
    data = {"autosalons": autosalon_object}
    car_object.autosalons.set([autosalon_object])
    filter_data = CarFilter(data=data)
    assert filter_data.qs.first().autosalons == car_object.autosalons


@pytest.mark.django_db
def test_car_model_options(car_object, option_car_object):
    data = {"options": option_car_object}
    car_object.options.set([option_car_object])
    filter_data = CarFilter(data=data)
    assert filter_data.qs.first().options == car_object.options


@pytest.mark.django_db
def test_option_car_year(option_car_object):
    data = {"year": str(option_car_object.year.year)}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().year == option_car_object.year


@pytest.mark.django_db
def test_option_car_mileage(option_car_object):
    data = {"mileage": 10000}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().mileage == option_car_object.mileage


@pytest.mark.django_db
def test_option_car_body_type(option_car_object):
    data = {"body_type": "sedan"}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().body_type == option_car_object.body_type


@pytest.mark.django_db
def test_option_car_transmission_type(option_car_object):
    data = {"transmission_type": "automatic"}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().transmission_type == option_car_object.transmission_type


@pytest.mark.django_db
def test_option_car_drive_unit_type(option_car_object):
    data = {"drive_unit_type": "complete"}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().drive_unit_type == option_car_object.drive_unit_type


@pytest.mark.django_db
def test_option_car_color(option_car_object):
    data = {"color": "blue"}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().color == option_car_object.color


@pytest.mark.django_db
def test_option_car_engine_type(option_car_object):
    data = {"engine_type": "petrol"}
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().engine_type == option_car_object.engine_type


@pytest.mark.django_db
def test_option_car_cars(option_car_object, car_object):
    data = {"cars": car_object}
    option_car_object.cars.set([car_object])
    filter_data = OptionCarFilter(data=data)
    assert filter_data.qs.first().cars == option_car_object.cars


@pytest.mark.django_db
def test_supplier_name(supplier_object):
    data = {"name": "AutoHouse"}
    filter_data = SupplierFilter(data=data)
    assert filter_data.qs.first().name == supplier_object.name


@pytest.mark.django_db
def test_supplier_price(supplier_object):
    data = {"price": 50000.00}
    filter_data = SupplierFilter(data=data)
    assert filter_data.qs.first().price == supplier_object.price


@pytest.mark.django_db
def test_supplier_cars(supplier_object, car_object):
    data = {"cars": car_object}
    supplier_object.cars.set([car_object])
    filter_data = SupplierFilter(data=data)
    assert filter_data.qs.first().cars == supplier_object.cars


@pytest.mark.django_db
def test_sale_history_autosalon(sale_history_object, autosalon_object):
    data = {"autosalon__name": autosalon_object.name}
    filter_data = SaleHistoryFilter(data=data)
    assert filter_data.qs.first().autosalon == sale_history_object.autosalon


@pytest.mark.django_db
def test_sale_history_supplier(sale_history_object, supplier_object):
    data = {"supplier__name": supplier_object.name}
    filter_data = SaleHistoryFilter(data=data)
    assert filter_data.qs.first().supplier == sale_history_object.supplier


@pytest.mark.django_db
def test_sale_history_price(sale_history_object):
    data = {"price": 50000.00}
    filter_data = SaleHistoryFilter(data=data)
    assert filter_data.qs.first().price == sale_history_object.price


@pytest.mark.django_db
def test_special_offer_of_autosalon_name(special_offer_of_autosalon_object):
    data = {"name": "Sale 25%"}
    filter_data = SpecialOfferOfAutoSalonFilter(data=data)
    assert filter_data.qs.first().name == special_offer_of_autosalon_object.name


@pytest.mark.django_db
def test_special_offer_of_autosalon_dealer(special_offer_of_autosalon_object, autosalon_object):
    data = {"dealer__name": autosalon_object.name}
    filter_data = SpecialOfferOfAutoSalonFilter(data=data)
    assert filter_data.qs.first().dealer == special_offer_of_autosalon_object.dealer


@pytest.mark.django_db
def test_special_offer_of_autosalon_discount(special_offer_of_autosalon_object):
    data = {"discount": 25}
    filter_data = SpecialOfferOfAutoSalonFilter(data=data)
    assert filter_data.qs.first().discount == special_offer_of_autosalon_object.discount


@pytest.mark.django_db
def test_special_offer_of_autosalon_start_date(special_offer_of_autosalon_object):
    data = {"start_date": str(special_offer_of_autosalon_object.start_date.year)}
    filter_data = SpecialOfferOfAutoSalonFilter(data=data)
    assert filter_data.qs.first().start_date == special_offer_of_autosalon_object.start_date


@pytest.mark.django_db
def test_special_offer_of_autosalon_end_date(special_offer_of_autosalon_object):
    data = {"end_date": str(special_offer_of_autosalon_object.end_date.year)}
    filter_data = SpecialOfferOfAutoSalonFilter(data=data)
    assert filter_data.qs.first().end_date == special_offer_of_autosalon_object.end_date


@pytest.mark.django_db
def test_special_offer_of_supplier_name(special_offer_of_supplier_object):
    data = {"name": "Sale 25%"}
    filter_data = SpecialOfferOfSupplierFilter(data=data)
    assert filter_data.qs.first().name == special_offer_of_supplier_object.name


@pytest.mark.django_db
def test_special_offer_of_supplier_supplier(special_offer_of_supplier_object, supplier_object):
    data = {"supplier__name": supplier_object.name}
    filter_data = SpecialOfferOfSupplierFilter(data=data)
    assert filter_data.qs.first().supplier == special_offer_of_supplier_object.supplier


@pytest.mark.django_db
def test_special_offer_of_supplier_discount(special_offer_of_supplier_object):
    data = {"discount": 25}
    filter_data = SpecialOfferOfSupplierFilter(data=data)
    assert filter_data.qs.first().discount == special_offer_of_supplier_object.discount


@pytest.mark.django_db
def test_special_offer_of_supplier_start_date(special_offer_of_supplier_object):
    data = {"start_date": str(special_offer_of_supplier_object.start_date.year)}
    filter_data = SpecialOfferOfSupplierFilter(data=data)
    assert filter_data.qs.first().start_date == special_offer_of_supplier_object.start_date


@pytest.mark.django_db
def test_special_offer_of_supplier_end_date(special_offer_of_supplier_object):
    data = {"end_date": str(special_offer_of_supplier_object.end_date.year)}
    filter_data = SpecialOfferOfSupplierFilter(data=data)
    assert filter_data.qs.first().end_date == special_offer_of_supplier_object.end_date