from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from django_dynamic_fixture import G
from rest_framework import status
from rest_framework.test import APITestCase


from users.models import Customer

from ..models import (
    AutoSalon,
    Supplier,
    Car,
    OptionCar,
    SaleHistory,
    SpecialOfferOfAutoSalon,
    SpecialOfferOfSupplier,
)
from ..serializers import (
    AutoSalonSerializer,
    CarSerializer,
    OptionCarSerializer,
    SupplierSerializer,
    SaleHistorySerializer,
    SpecialOfferOfAutoSalonSerializer,
    SpecialOfferOfSupplierSerializer,
)


class AutoSaLonViewSetTestCase(APITestCase):
    """
    APITestCase for AutoSalonViewSet
    """

    def setUp(self):
        self.supplier = G(
            model=Supplier,
            name="AutoHouse",
            year_of_issue=timezone.now(),
            price=50000.00,
        )

        self.car = G(model=Car, model_name="BMW M5 G30 Рестайлинг")

        self.customer = G(Customer, first_name="Boris")

        self.autosalon = G(
            model=AutoSalon,
            name="WestCoastCustoms",
            location="US",
            balance=100000.00,
            suppliers=[self.supplier],
            customers=[],
        )
        self.autosalon2 = G(
            model=AutoSalon,
            name="AutoHouse",
            location="ES",
            balance=100000.00,
            suppliers=[self.supplier],
            customers=[],
        )

    def test_autosalon_list(self):
        response = self.client.get(path=reverse(viewname="autosalons-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AutoSalonSerializer(
            [self.autosalon, self.autosalon2], many=True
        ).data
        self.assertListEqual(response.data, serializer_data)

    def test_autosalon_create(self):
        data = {
            "name": "Test Autosalon",
            "location": "US",
            "balance": 100000.00,
            "suppliers": [self.supplier.id],
            "customers": [self.customer.id],
        }
        response = self.client.post(path=reverse(viewname="autosalons-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        autosalon = AutoSalon.autosalons.get(name="Test Autosalon")
        self.assertEqual(response.data["name"], autosalon.name)

    def test_autosalon_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="autosalons-detail", args=[self.autosalon.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AutoSalonSerializer(self.autosalon).data
        self.assertEqual(response.data, serializer_data)

    def test_autosalon_update(self):
        data = {
            "name": "EastCoastCustoms",
            "location": "US",
            "balance": 10000.00,
            "suppliers": [self.supplier.id],
            "customers": [self.customer.id],
        }
        response = self.client.put(
            path=reverse(viewname="autosalons-detail", args=[self.autosalon.id]),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        autosalon = AutoSalon.autosalons.get(id=self.autosalon.id)
        self.assertEqual(autosalon.name, "EastCoastCustoms")

    def test_autosalon_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="autosalons-detail", args=[self.autosalon2.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AutoSalon.autosalons.filter(id=self.autosalon2.id).exists())


class CarTestCase(APITestCase):
    """
    APITestCase for CarViewSet
    """

    def setUp(self):
        self.autosalon = G(
            model=AutoSalon,
            name="WestCoastCustoms",
            location="US",
            balance=100000.00,
        )
        self.option_car = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=5000,
            body_type="sedan",
            transmission_type="automatic",
            drive_unit_type="complete",
            color="red",
            engine_type="petrol",
        )

        self.car1 = G(
            model=Car,
            model_name="BMW M5 G30",
            autosalons=[self.autosalon],
            options=[self.option_car],
        )
        self.car2 = G(
            model=Car,
            model_name="Mercedes-Benz E63 AMG",
            autosalons=[self.autosalon],
            options=[self.option_car],
        )

    def test_car_list(self):
        response = self.client.get(path=reverse(viewname="cars-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = CarSerializer([self.car1, self.car2], many=True).data
        self.assertListEqual(response.data, serializer_data)

    def test_car_create(self):
        data = {
            "model_name": "Lamborghini Huracan Performance",
            "autosalons": [self.autosalon.id],
            "options": [self.option_car.id],
        }
        response = self.client.post(path=reverse(viewname="cars-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_car_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="cars-detail", args=[self.car1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = CarSerializer(self.car1).data
        self.assertEqual(response.data, serializer_data)

    def test_car_update(self):
        data = {
            "model_name": "BMW X5 M G30",
            "autosalons": [self.autosalon.id],
            "options": [self.option_car.id],
        }
        response = self.client.put(
            path=reverse(viewname="cars-detail", args=[self.car1.id]), data=data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        car = Car.cars.get(id=self.car1.id)
        self.assertEqual(car.model_name, "BMW X5 M G30")

    def test_car_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="cars-detail", args=[self.car2.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AutoSalon.autosalons.filter(id=self.car2.id).exists())


class OptionCarTestCase(APITestCase):
    """
    APITestCase for OptionViewSet
    """

    def setUp(self):
        self.car1 = G(model=Car, model_name="BMW M8 G30")
        self.car2 = G(model=Car, model_name="Mercedes-Benz E63 AMG")

        self.option_car1 = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=12000,
            body_type="sedan",
            transmission_type="automatic",
            drive_unit_type="complete",
            color="red",
            engine_type="petrol",
            cars=[self.car2, self.car1],
        )
        self.option_car2 = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=10000,
            body_type="coupe",
            transmission_type="automatic",
            drive_unit_type="back",
            color="blue",
            engine_type="diesel",
            cars=[self.car1, self.car2],
        )
        self.option_car3 = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=100000,
            body_type="suv",
            transmission_type="mechanics",
            drive_unit_type="front",
            color="orange",
            engine_type="electro",
            cars=[self.car1, self.car2],
        )

    def test_option_car_list(self):
        response = self.client.get(path=reverse(viewname="options-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = OptionCarSerializer(
            [self.option_car1, self.option_car2, self.option_car3], many=True
        ).data
        serializer_mileages = [item.get("mileage") for item in serializer_data]
        response_mileages = [item.get("mileage") for item in response.data]

        self.assertListEqual(response_mileages, serializer_mileages)

    def test_option_car_create(self):
        data = {
            "year": timezone.now(),
            "mileage": 120000,
            "body_type": "sport",
            "transmission_type": "mechanics",
            "drive_unit_type": "front",
            "color": "orange",
            "engine_type": "petrol",
            "cars": [self.car1.id, self.car2.id],
        }
        response = self.client.post(path=reverse(viewname="options-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_option_car_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="options-detail", args=[self.option_car1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = OptionCarSerializer(self.option_car1).data
        serializer_body_type = serializer_data.get("body_type")
        response_body_type = response.data.get("body_type")

        self.assertEqual(response_body_type, serializer_body_type)

    def test_option_car_update(self):
        data = {
            "year": timezone.now(),
            "mileage": 120000,
            "body_type": "pickup",
            "transmission_type": "mechanics",
            "drive_unit_type": "front",
            "color": "orange",
            "engine_type": "electro",
            "cars": [self.car1.id, self.car2.id],
        }
        response = self.client.put(
            path=reverse(viewname="options-detail", args=[self.option_car2.id]),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        option_car = OptionCar.options.get(mileage=120000)
        self.assertEqual(option_car.mileage, 120000)

    def test_option_car_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="options-detail", args=[self.option_car3.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(OptionCar.options.filter(body_type="suv").exists())


class SupplierTestCase(APITestCase):
    """
    APITestCase for SupplierVewSet
    """

    def setUp(self):
        self.car = G(model=Car, model_name="Volkswagen Arteon")

        self.supplier1 = G(
            model=Supplier,
            name="AutoHouse",
            year_of_issue=timezone.now(),
            price=25000.00,
            cars=[self.car],
        )
        self.supplier2 = G(
            model=Supplier,
            name="Atlant-M",
            year_of_issue=timezone.now(),
            price=15000.00,
            cars=[self.car],
        )
        self.supplier3 = G(
            model=Supplier,
            name="CarHouse",
            year_of_issue=timezone.now(),
            price=45000.00,
            cars=[self.car],
        )

    def test_supplier_list(self):
        response = self.client.get(path=reverse(viewname="suppliers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SupplierSerializer(
            [self.supplier1, self.supplier2, self.supplier3], many=True
        ).data
        serializer_names = [item.get("name") for item in serializer_data]
        response_names = [item.get("name") for item in response.data]

        self.assertListEqual(response_names, serializer_names)

    def test_supplier_create(self):
        data = {
            "name": "Test Supplier",
            "year_of_issue": timezone.now(),
            "price": 15000.00,
            "cars": [self.car.id],
        }
        response = self.client.post(path=reverse(viewname="suppliers-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_supplier_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="suppliers-detail", args=[self.supplier1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SupplierSerializer(self.supplier1).data
        serializer_name = serializer_data.get("name")
        response_name = response.data.get("name")

        self.assertEqual(response_name, serializer_name)

    def test_supplier_update(self):
        data = {
            "name": "Test Supplier2",
            "year_of_issue": timezone.now(),
            "price": 15000.00,
            "cars": [self.car.id],
        }
        response = self.client.put(
            path=reverse(viewname="suppliers-detail", args=[self.supplier2.id]),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK),
        supplier = Supplier.suppliers.get(name="Test Supplier2")
        self.assertEqual(supplier.name, "Test Supplier2")

    def test_supplier_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="suppliers-detail", args=[self.supplier3.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Supplier.suppliers.filter(name="CarHouse").exists())


class SaleHistoryTestCase(APITestCase):
    """
    APITestCase for SaleHistoryViewSet
    """

    def setUp(self):
        self.autosalon = G(
            model=AutoSalon, name="WestCoastCustoms", location="US", balance=100000.00
        )

        self.supplier = G(
            Supplier, name="AutoHouse", year_of_issue=timezone.now(), price=25000.00
        )

        self.sale_history1 = G(
            SaleHistory,
            autosalon=self.autosalon,
            supplier=self.supplier,
            price=15000.00,
        )
        self.sale_history2 = G(
            SaleHistory,
            autosalon=self.autosalon,
            supplier=self.supplier,
            price=20000.00,
        )
        self.sale_history3 = G(
            SaleHistory,
            autosalon=self.autosalon,
            supplier=self.supplier,
            price=35000.00,
        )

    def test_sale_history_list(self):
        response = self.client.get(path=reverse(viewname="histories-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistorySerializer(
            [self.sale_history1, self.sale_history2, self.sale_history3], many=True
        ).data
        serializer_prices = [item.get("price") for item in serializer_data]
        response_prices = [item.get("price") for item in response.data]

        self.assertListEqual(response_prices, serializer_prices)

    def test_sale_history_create(self):
        data = {
            "autosalon": self.autosalon.id,
            "supplier": self.supplier.id,
            "price": 25000.00,
        }
        response = self.client.post(path=reverse(viewname="histories-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sale_history_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="histories-detail", args=[self.sale_history1.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistorySerializer(self.sale_history1).data
        serializer_price = serializer_data.get("price")
        response_price = response.data.get("price")

        self.assertEqual(response_price, serializer_price)

    def test_sale_history_update(self):
        data = {
            "autosalon": self.autosalon.id,
            "supplier": self.supplier.id,
            "price": 125000.00,
        }
        response = self.client.put(
            path=reverse(viewname="histories-detail", args=[self.sale_history2.id]),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sale_history = SaleHistory.sale_histories.get(price=125000.00)
        self.assertEqual(sale_history.price, 125000.00)

    def test_sale_history_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="histories-detail", args=[self.sale_history3.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SaleHistory.sale_histories.filter(price=35000.00).exists())


class SpecialOfferOfAutoSalonTestCase(APITestCase):
    """
    APITestCase for SpecialOfferOfAutoSalonViewSet
    """

    def setUp(self):
        self.autosalon = G(
            model=AutoSalon, name="WestCoastCustoms", location="US", balance=100000.00
        )
        self.autosalon2 = G(
            model=AutoSalon, name="AutoHouse", location="US", balance=10000.00
        )

        self.special_offer_of_autosalon1 = G(
            model=SpecialOfferOfAutoSalon,
            name="Sale 20%",
            descr="Special offer for customers!",
            discount=2000,
            dealer=self.autosalon,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.special_offer_of_autosalon2 = G(
            model=SpecialOfferOfAutoSalon,
            name="Sale 30%",
            descr="Special offer for customers!",
            discount=5000,
            dealer=self.autosalon2,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.special_offer_of_autosalon3 = G(
            model=SpecialOfferOfAutoSalon,
            name="Sale 60%",
            descr="Special offer for customers!",
            discount=25000,
            dealer=self.autosalon2,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )

    def test_special_offer_of_autosalon_list(self):
        response = self.client.get(path=reverse(viewname="offers_autosalon-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SpecialOfferOfAutoSalonSerializer(
            [
                self.special_offer_of_autosalon1,
                self.special_offer_of_autosalon2,
                self.special_offer_of_autosalon3,
            ],
            many=True,
        ).data
        serializer_names = [item.get("name") for item in serializer_data]
        response_names = [item.get("name") for item in response.data]

        self.assertListEqual(response_names, serializer_names)

    def test_special_offer_of_autosalon_create(self):
        data = {
            "name": "Sale 20%",
            "descr": "Special offer for autosalons!",
            "discount": 2000,
            "dealer": self.autosalon.id,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=7),
        }
        response = self.client.post(reverse("offers_autosalon-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_special_offer_of_autosalon_retrieve(self):
        response = self.client.get(
            path=reverse(
                viewname="offers_autosalon-detail",
                args=[self.special_offer_of_autosalon2.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SpecialOfferOfAutoSalonSerializer(
            self.special_offer_of_autosalon2
        ).data
        serializer_name = serializer_data.get("name")
        response_name = response.data.get("name")

        self.assertEqual(response_name, serializer_name)

    def test_special_offer_of_autosalon_update(self):
        data = {
            "name": "Sale 50%",
            "descr": "Special offer for autosalons!",
            "discount": 10000,
            "dealer": self.autosalon.id,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=7),
        }
        response = self.client.put(
            path=reverse(
                viewname="offers_autosalon-detail",
                args=[self.special_offer_of_autosalon2.id],
            ),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        special_offer = SpecialOfferOfAutoSalon.special_offer_of_autosalon.get(
            name="Sale 50%"
        )
        self.assertEqual(special_offer.name, "Sale 50%")

    def test_special_offer_of_autosalon_destroy(self):
        response = self.client.delete(
            path=reverse(
                viewname="offers_autosalon-detail",
                args=[self.special_offer_of_autosalon3.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            SpecialOfferOfAutoSalon.special_offer_of_autosalon.filter(
                name="Sale 60%"
            ).exists()
        )


class SpecialOfferOfSupplierTestCase(APITestCase):
    """
    APITestCase for SpecialOfferOfSupplierViewSet
    """

    def setUp(self):
        self.supplier = G(
            model=Supplier,
            name="AutoHouse",
            year_of_issue=timezone.now(),
            price=25000.00,
        )
        self.supplier2 = G(
            model=Supplier,
            name="Atlant-M",
            year_of_issue=timezone.now(),
            price=15000.00,
        )

        self.special_offer_of_supplier1 = G(
            model=SpecialOfferOfSupplier,
            id=1,
            name="Sale 20%",
            descr="Special offer for autosalons!",
            discount=2000,
            supplier=self.supplier,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.special_offer_of_supplier2 = G(
            model=SpecialOfferOfSupplier,
            id=2,
            name="Sale 30%",
            descr="Special offer for autosalons!",
            discount=5000,
            supplier=self.supplier2,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.special_offer_of_supplier3 = G(
            model=SpecialOfferOfSupplier,
            id=3,
            name="Sale 60%",
            descr="Special offer for suppliers!",
            discount=25000,
            supplier=self.supplier,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )

    def test_special_offer_of_supplier_list(self):
        response = self.client.get(path=reverse(viewname="offers_customer-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SpecialOfferOfSupplierSerializer(
            [
                self.special_offer_of_supplier1,
                self.special_offer_of_supplier2,
                self.special_offer_of_supplier3,
            ],
            many=True,
        ).data
        serializer_names = [item.get("name") for item in serializer_data]
        response_names = [item.get("name") for item in response.data]

        self.assertListEqual(response_names, serializer_names)

    def test_special_offer_of_supplier_create(self):
        data = {
            "name": "Sale 20%",
            "descr": "Special offer for autosalons!",
            "discount": 2000,
            "supplier": self.supplier2.id,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=7),
        }
        response = self.client.post(reverse("offers_customer-list"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_special_offer_of_supplier_retrieve(self):
        response = self.client.get(
            path=reverse(
                viewname="offers_customer-detail",
                args=[self.special_offer_of_supplier2.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = SpecialOfferOfSupplierSerializer(
            self.special_offer_of_supplier2
        ).data
        serializer_name = serializer_data.get("name")
        response_name = response.data.get("name")

        self.assertEqual(response_name, serializer_name)

    def test_special_offer_of_supplier_update(self):
        data = {
            "name": "Sale 50%",
            "descr": "Special offer for autosalons!",
            "discount": 10000,
            "supplier": self.supplier.id,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=7),
        }
        response = self.client.put(
            path=reverse(
                viewname="offers_customer-detail",
                args=[self.special_offer_of_supplier2.id],
            ),
            data=data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        special_offer = SpecialOfferOfSupplier.special_offer_of_supplier.get(
            name="Sale 50%"
        )
        self.assertEqual(special_offer.name, "Sale 50%")

    def test_special_offer_of_supplier_destroy(self):
        response = self.client.delete(
            path=reverse(
                viewname="offers_customer-detail",
                args=[self.special_offer_of_supplier3.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            SpecialOfferOfSupplier.special_offer_of_supplier.filter(
                name="Sale 60%"
            ).exists()
        )
