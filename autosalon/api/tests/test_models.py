import datetime

from django.test import TestCase
from django_dynamic_fixture import G, F

from ..models import (
    AutoSalon,
    Car,
    OptionCar,
    Supplier,
    SaleHistory,
    SpecialOfferOfSupplier,
    SpecialOfferOfAutoSalon,
)


class AutoSalonTestCase(TestCase):
    """
    TestCase fo AutoSalon's model
    """

    def test_auto_salon_name(self):
        """
        Test of check location's value
        :return:
        """
        autosalon = G(AutoSalon, name="WestCoastCustoms")
        self.assertEqual(autosalon.name, "WestCoastCustoms"),
        self.assertNotEqual(autosalon.name, "AutoSalon №1")

    def test_auto_salon_location(self):
        """
        Test of check location's value
        :return:
        """
        autosalon = G(AutoSalon, location="US")
        self.assertEqual(autosalon.location, "US")
        self.assertNotEqual(autosalon.location, "Bel")

    def test_auto_salon_balance(self):
        """
        Test of check location's value
        :return:
        """
        autosalon = G(AutoSalon, balance=100000.0)
        self.assertEqual(autosalon.balance, 100000.0)
        self.assertNotEqual(autosalon.balance, 10000.00)

    def test_auto_salon_suppliers(self):
        """
        Test of check supplier's value
        :return:
        """
        supplier1 = G(Supplier)
        supplier2 = G(Supplier)
        autosalon = G(AutoSalon, suppliers=[supplier1, supplier2])
        self.assertEqual(autosalon.suppliers.count(), 2)
        self.assertNotEqual(autosalon.suppliers.count(), 1)

    def test_auto_salon_customers(self):
        """
        Test of check customer's value
        :return:
        """
        autosalon = G(
            AutoSalon, customers=[F(username="Customer"), F(username="Admin")]
        )
        self.assertEqual(autosalon.customers.count(), 2)
        self.assertNotEqual(autosalon.customers.count(), 1)


class CarTestCase(TestCase):
    """
    TestCase of check Car's model
    """

    def test_car_model(self):
        """
        Test of check model's value
        :return:
        """
        car = G(model=Car, model_name="BMW M5 G30")
        self.assertEqual(car.model_name, "BMW M5 G30")
        self.assertNotEqual(car.model_name, "Lamborghini Huracan Performante")

    def test_car_autosalons(self):
        """
        Test of check name's value
        :return:
        """
        autosalon1 = G(AutoSalon, name="WestCoastCustoms")
        autosalon2 = G(AutoSalon, name="Belarus №1")
        autosalon3 = G(AutoSalon, name="AutoHouse")
        car = G(Car, autosalons=[autosalon1, autosalon2, autosalon3])
        self.assertEqual(car.autosalons.count(), 3)
        self.assertNotEqual(car.autosalons.count(), 1)

    def test_car_options(self):
        """
        Test of check option's value
        :return:
        """
        option1 = G(OptionCar)
        car = G(Car, options=[option1])
        self.assertEqual(car.options.count(), 1)
        self.assertNotEqual(car.options.count(), 3)


class OptionCarTestCase(TestCase):
    """
    TestCase of OptionCar's model
    """

    def test_option_car_year(self):
        """
        Test of check year's value
        :return:
        """
        option_car = G(OptionCar, year=datetime.date(2023, 12, 10))
        self.assertEqual(option_car.year, datetime.date(2023, 12, 10))
        self.assertNotEqual(option_car.year, datetime.date(2020, 5, 20))

    def test_option_car_mileage(self):
        """
        Test of check mileage's value
        :return:
        """
        option_car = G(OptionCar, mileage=55000)
        self.assertEqual(option_car.mileage, 55000)
        self.assertNotEqual(option_car.mileage, 1000)
        self.assertNotEqual(option_car.mileage, -1000)

    def test_option_car_body_type(self):
        """
        Test of check body_type's value
        :return:
        """
        option_car = G(OptionCar, body_type="Sedan")
        self.assertEqual(option_car.body_type, "Sedan")
        self.assertNotEqual(option_car.body_type, "SUV")

    def test_option_car_transmission_type(self):
        """
        Test of check transmission_type's value
        :return:
        """
        option_car = G(OptionCar, transmission_type="Automatic")
        self.assertEqual(option_car.transmission_type, "Automatic")
        self.assertNotEqual(option_car.transmission_type, "Mechanic")

    def test_option_car_drive_unit_type(self):
        """
        Test of check drive_unit_type's value
        :return:
        """
        option_car = G(OptionCar, drive_unit_type="Complete")
        self.assertEqual(option_car.drive_unit_type, "Complete")
        self.assertNotEqual(option_car.drive_unit_type, "Front")

    def test_option_car_color(self):
        """
        Test of check car_color's value
        :return:
        """
        option_car = G(OptionCar, color="Blue")
        self.assertEqual(option_car.color, "Blue")
        self.assertNotEqual(option_car.color, "Red")

    def test_option_car_engine_type(self):
        """
        Test of check engine_type's value
        :return:
        """
        option_car = G(OptionCar, engine_type="Petrol")
        self.assertEqual(option_car.engine_type, "Petrol")
        self.assertNotEqual(option_car.engine_type, "Diesel")

    def test_option_car_cars(self):
        """
        Test of check car's value
        :return:
        """
        car1 = G(Car, model_name="BMW M5 G30")
        car2 = G(Car, model_name="AUDI RS6 C8")
        car3 = G(Car, model_name="Lamborghini Huracan Performante")
        option_car = G(OptionCar, cars=[car1, car2, car3])
        self.assertEqual(option_car.cars.count(), 3)
        self.assertNotEqual(option_car.cars.count(), 4)


class SupplierTestCase(TestCase):
    """
    TestCase of OptionCar's model
    """

    def test_supplier_name(self):
        """
        Test of check name's value
        :return:
        """
        supplier = G(Supplier, name="GrandMotors")
        self.assertEqual(supplier.name, "GrandMotors")
        self.assertNotEqual(supplier.name, "CustomAuto")

    def test_supplier_year_of_issue(self):
        """
        Test of check year_of_issue's value
        :return:
        """
        supplier = G(Supplier, year_of_issue=datetime.date(2023, 10, 2))
        self.assertEqual(supplier.year_of_issue, datetime.date(2023, 10, 2))
        self.assertNotEqual(supplier.year_of_issue, datetime.date(2023, 1, 31))

    def test_supplier_price(self):
        """
        Test of check price's value
        :return:
        """
        supplier = G(Supplier, price=50000.0)
        self.assertEqual(supplier.price, 50000.0)
        self.assertNotEqual(supplier.price, 10000.00)

    def test_supplier_cars(self):
        """
        Test of check car's value
        :return:
        """
        supplier = G(Supplier, cars=3)
        self.assertEqual(supplier.cars.count(), 3)
        self.assertNotEqual(supplier.cars.count(), 5)


class SaleHistoryTestCase(TestCase):
    """
    TestCase of SaleHistory's model
    """

    def test_sale_history_autosalons(self):
        """
        Test of check autosalon's value
        :return:
        """
        autosalon = G(AutoSalon, name="WestCoastCustoms")
        sale_history = G(SaleHistory, autosalon=autosalon)
        self.assertEqual(sale_history.autosalon.name, "WestCoastCustoms")
        self.assertNotEqual(sale_history.autosalon.name, "AutoHouse")

    def test_sale_history_supplier(self):
        """
        Test of check supplier's value
        :return:
        """
        supplier = G(Supplier, name="GrandMotors")
        sale_history = G(SaleHistory, supplier=supplier)
        self.assertEqual(sale_history.supplier.name, "GrandMotors")
        self.assertNotEqual(sale_history.supplier.name, "CustomAuto")

    def test_sale_history_price(self):
        """
        Test of check price's value
        :return:
        """
        sale_history = G(SaleHistory, price=25000.0)
        self.assertEqual(sale_history.price, 25000.0)
        self.assertNotEqual(sale_history.price, 35000.00)


class SpecialOfferOfSupplierTestCase(TestCase):
    """
    TestCase of SpecialOfferOfSupplier's model
    """

    def test_special_offer_of_supplier_name(self):
        """
        Test of check name's value
        :return:
        """
        special_offer_of_supplier = G(SpecialOfferOfSupplier, name="20% for all cars")
        self.assertEqual(special_offer_of_supplier.name, "20% for all cars")
        self.assertNotEqual(special_offer_of_supplier.name, "5% for BMW M5 G30")

    def test_special_offer_of_supplier_description(self):
        """
        Test of check description's value
        :return:
        """
        special_offer_of_supplier = G(SpecialOfferOfSupplier, descr="20% for all cars")
        self.assertEqual(special_offer_of_supplier.descr, "20% for all cars")
        self.assertNotEqual(special_offer_of_supplier.descr, "5% for BMW M5 G30")

    def test_special_offer_of_supplier_discount(self):
        """
        Test of check discount's value
        :return:
        """
        special_offer_of_supplier = G(SpecialOfferOfSupplier, discount=10)
        self.assertEqual(special_offer_of_supplier.discount, 10)
        self.assertNotEqual(special_offer_of_supplier.discount, 15)
        self.assertNotEqual(special_offer_of_supplier.discount, -15)

    def test_special_offer_of_supplier_supplier(self):
        """
        Test of check supplier's value
        :return:
        """
        special_offer_of_supplier = G(
            SpecialOfferOfSupplier, supplier=F(name="GrandMotors")
        )
        self.assertEqual(special_offer_of_supplier.supplier.name, "GrandMotors")
        self.assertNotEqual(special_offer_of_supplier.supplier.name, "CustomAuto")

    def test_special_offer_of_supplier_start_date(self):
        """
        Test of check start_date's value
        :return:
        """
        special_offer_of_supplier = G(
            SpecialOfferOfSupplier, start_date=datetime.date(2023, 10, 2)
        )
        self.assertEqual(
            special_offer_of_supplier.start_date, datetime.date(2023, 10, 2)
        )
        self.assertNotEqual(
            special_offer_of_supplier.start_date, datetime.date(2022, 11, 10)
        )

    def test_special_offer_of_supplier_end_date(self):
        """
        Test of check end_date's value
        :return:
        """
        special_offer_of_supplier = G(
            SpecialOfferOfSupplier, end_date=datetime.date(2023, 10, 2)
        )
        self.assertEqual(special_offer_of_supplier.end_date, datetime.date(2023, 10, 2))
        self.assertNotEqual(
            special_offer_of_supplier.end_date, datetime.date(2023, 12, 25)
        )


class SpecialOfferOfAutoSalonTestCase(TestCase):
    """
    TestCase of SpecialOfferOfAutoSalon's model
    """

    def test_special_offer_of_autosalon_name(self):
        """
        Test of check name's value
        :return:
        """
        special_offer_of_autosalon = G(SpecialOfferOfAutoSalon, name="20% for all cars")
        self.assertEqual(special_offer_of_autosalon.name, "20% for all cars")
        self.assertNotEqual(special_offer_of_autosalon.name, "5% for BMW M5 G30")

    def test_special_offer_of_autosalon_description(self):
        """
        Test of check description's value
        :return:
        """
        special_offer_of_autosalon = G(
            SpecialOfferOfAutoSalon, descr="20% for all cars"
        )
        self.assertEqual(special_offer_of_autosalon.descr, "20% for all cars")
        self.assertNotEqual(special_offer_of_autosalon.descr, "5% for BMW M5 G30")

    def test_special_offer_of_autosalon_discount(self):
        """
        Test of check discount's value
        :return:
        """
        special_offer_of_autosalon = G(SpecialOfferOfAutoSalon, discount=10)
        self.assertEqual(special_offer_of_autosalon.discount, 10)
        self.assertNotEqual(special_offer_of_autosalon.discount, 15)
        self.assertNotEqual(special_offer_of_autosalon.discount, -15)

    def test_special_offer_of_autosalon_dealer(self):
        """
        Test of check dealer's value
        :return:
        """
        autosalon = G(AutoSalon, name="WestCoastCustoms")
        special_offer_of_autosalon = G(SpecialOfferOfAutoSalon, dealer=autosalon)
        self.assertEqual(special_offer_of_autosalon.dealer.name, "WestCoastCustoms")
        self.assertNotEqual(special_offer_of_autosalon.dealer.name, "AutoHouse")

    def test_special_offer_of_autosalon_start_date(self):
        """
        Test of check start_date's value
        :return:
        """
        special_offer_of_autosalon = G(
            SpecialOfferOfAutoSalon, start_date=datetime.date(2023, 10, 2)
        )
        self.assertEqual(
            special_offer_of_autosalon.start_date, datetime.date(2023, 10, 2)
        )
        self.assertNotEqual(
            special_offer_of_autosalon.start_date, datetime.date(2023, 12, 25)
        )

    def test_special_offer_of_autosalon_end_date(self):
        """
        Test of check end_date's value
        :return:
        """
        special_offer_of_autosalon = G(
            SpecialOfferOfAutoSalon, end_date=datetime.date(2023, 10, 2)
        )
        self.assertEqual(
            special_offer_of_autosalon.end_date, datetime.date(2023, 10, 2)
        )
        self.assertNotEqual(
            special_offer_of_autosalon.end_date, datetime.date(2023, 12, 25)
        )
