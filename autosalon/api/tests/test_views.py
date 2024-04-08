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

        self.first_autosalon = G(
            model=AutoSalon,
            name="WestCoastCustoms",
            location="US",
            balance=100000.00,
            suppliers=[self.supplier],
            customers=[],
        )
        self.second_autosalon = G(
            model=AutoSalon,
            name="AutoHouse",
            location="ES",
            balance=100000.00,
            suppliers=[self.supplier],
            customers=[],
        )
        self.autosalon_data = {
            "name": "Test Autosalon",
            "location": "US",
            "balance": 100000.00,
            "suppliers": [self.supplier.id],
            "customers": [self.customer.id],
        }

    def test_autosalon_list(self):
        response = self.client.get(path=reverse(viewname="autosalons-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AutoSalonSerializer(
            [self.first_autosalon, self.second_autosalon], many=True
        ).data
        self.assertListEqual(response.data, serializer_data)

    def test_autosalon_create(self):
        response = self.client.post(
            path=reverse(viewname="autosalons-list"), data=self.autosalon_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        autosalon = AutoSalon.objects.get(name="Test Autosalon")
        self.assertEqual(response.data["name"], autosalon.name)

    def test_autosalon_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="autosalons-detail", args=[self.first_autosalon.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = AutoSalonSerializer(self.first_autosalon).data
        self.assertEqual(response.data, serializer_data)

    def test_autosalon_update(self):
        response = self.client.put(
            path=reverse(viewname="autosalons-detail", args=[self.first_autosalon.id]),
            data=self.autosalon_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        autosalon = AutoSalon.objects.get(id=self.first_autosalon.id)
        self.assertEqual(autosalon.name, "Test Autosalon")

    def test_autosalon_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="autosalons-detail", args=[self.second_autosalon.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AutoSalon.objects.filter(id=self.second_autosalon.id).exists())


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

        self.first_car = G(
            model=Car,
            model_name="BMW M5 G30",
            autosalons=[self.autosalon],
            options=[self.option_car],
        )
        self.second_car = G(
            model=Car,
            model_name="Mercedes-Benz E63 AMG",
            autosalons=[self.autosalon],
            options=[self.option_car],
        )
        self.car_data = {
            "model_name": "Lamborghini Huracan Performance",
            "autosalons": [self.autosalon.id],
            "options": [self.option_car.id],
        }

    def test_car_list(self):
        response = self.client.get(path=reverse(viewname="cars-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = CarSerializer(
            [self.first_car, self.second_car], many=True
        ).data
        self.assertListEqual(response.data, serializer_data)

    def test_car_create(self):
        response = self.client.post(
            path=reverse(viewname="cars-list"), data=self.car_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_car_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="cars-detail", args=[self.first_car.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = CarSerializer(self.first_car).data
        self.assertEqual(response.data, serializer_data)

    def test_car_update(self):
        response = self.client.put(
            path=reverse(viewname="cars-detail", args=[self.first_car.id]),
            data=self.car_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        car = Car.objects.get(id=self.first_car.id)
        self.assertEqual(car.model_name, "Lamborghini Huracan Performance")

    def test_car_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="cars-detail", args=[self.second_car.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Car.objects.filter(id=self.second_car.id).exists())


class OptionCarTestCase(APITestCase):
    """
    APITestCase for OptionViewSet
    """

    def setUp(self):
        self.first_car = G(model=Car, model_name="BMW M8 G30")
        self.second_car = G(model=Car, model_name="Mercedes-Benz E63 AMG")

        self.first_option_car = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=12000,
            body_type="sedan",
            transmission_type="automatic",
            drive_unit_type="complete",
            color="red",
            engine_type="petrol",
            cars=[self.second_car, self.first_car],
        )
        self.second_option_car = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=10000,
            body_type="coupe",
            transmission_type="automatic",
            drive_unit_type="back",
            color="blue",
            engine_type="diesel",
            cars=[self.first_car, self.second_car],
        )
        self.third_option_car = G(
            model=OptionCar,
            year=timezone.now(),
            mileage=100000,
            body_type="suv",
            transmission_type="mechanics",
            drive_unit_type="front",
            color="orange",
            engine_type="electro",
            cars=[self.first_car, self.second_car],
        )
        self.option_car_data = {
            "year": timezone.now(),
            "mileage": 120000,
            "body_type": "sport",
            "transmission_type": "mechanics",
            "drive_unit_type": "front",
            "color": "orange",
            "engine_type": "petrol",
            "cars": [self.first_car.id, self.second_car.id],
        }

    def test_option_car_list(self):
        response = self.client.get(path=reverse(viewname="options-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = OptionCarSerializer(
            [self.first_option_car, self.second_option_car, self.third_option_car],
            many=True,
        ).data
        serializer_mileages = [item.get("mileage") for item in serializer_data]
        response_mileages = [item.get("mileage") for item in response.data]

        self.assertListEqual(response_mileages, serializer_mileages)

    def test_option_car_create(self):
        response = self.client.post(
            path=reverse(viewname="options-list"), data=self.option_car_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_option_car_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="options-detail", args=[self.first_option_car.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = OptionCarSerializer(self.first_option_car).data
        serializer_body_type = serializer_data.get("body_type")
        response_body_type = response.data.get("body_type")

        self.assertEqual(response_body_type, serializer_body_type)

    def test_option_car_update(self):
        response = self.client.put(
            path=reverse(viewname="options-detail", args=[self.second_option_car.id]),
            data=self.option_car_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        option_car = OptionCar.objects.get(mileage=120000)
        self.assertEqual(option_car.mileage, 120000)

    def test_option_car_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="options-detail", args=[self.third_option_car.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(OptionCar.objects.filter(body_type="suv").exists())


class SupplierTestCase(APITestCase):
    """
    APITestCase for SupplierVewSet
    """

    def setUp(self):
        self.car = G(model=Car, model_name="Volkswagen Arteon")

        self.first_supplier = G(
            model=Supplier,
            name="AutoHouse",
            year_of_issue=timezone.now(),
            price=25000.00,
            cars=[self.car],
        )
        self.second_supplier = G(
            model=Supplier,
            name="Atlant-M",
            year_of_issue=timezone.now(),
            price=15000.00,
            cars=[self.car],
        )
        self.third_supplier = G(
            model=Supplier,
            name="CarHouse",
            year_of_issue=timezone.now(),
            price=45000.00,
            cars=[self.car],
        )
        self.supplier_data = {
            "name": "Test Supplier",
            "year_of_issue": timezone.now(),
            "price": 15000.00,
            "cars": [self.car.id],
        }

    def test_supplier_list(self):
        response = self.client.get(path=reverse(viewname="suppliers-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SupplierSerializer(
            [self.first_supplier, self.second_supplier, self.third_supplier], many=True
        ).data
        serializer_names = [item.get("name") for item in serializer_data]
        response_names = [item.get("name") for item in response.data]

        self.assertListEqual(response_names, serializer_names)

    def test_supplier_create(self):
        response = self.client.post(
            path=reverse(viewname="suppliers-list"), data=self.supplier_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_supplier_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="suppliers-detail", args=[self.first_supplier.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SupplierSerializer(self.first_supplier).data
        serializer_name = serializer_data.get("name")
        response_name = response.data.get("name")

        self.assertEqual(response_name, serializer_name)

    def test_supplier_update(self):
        response = self.client.put(
            path=reverse(viewname="suppliers-detail", args=[self.second_supplier.id]),
            data=self.supplier_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK),
        supplier = Supplier.objects.get(name="Test Supplier")
        self.assertEqual(supplier.name, "Test Supplier")

    def test_supplier_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="suppliers-detail", args=[self.third_supplier.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Supplier.objects.filter(name="CarHouse").exists())


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

        self.first_sale_history = G(
            SaleHistory,
            autosalon=self.autosalon,
            supplier=self.supplier,
            price=15000.00,
        )
        self.second_sale_history = G(
            SaleHistory,
            autosalon=self.autosalon,
            supplier=self.supplier,
            price=20000.00,
        )
        self.third_sale_history = G(
            SaleHistory,
            autosalon=self.autosalon,
            supplier=self.supplier,
            price=35000.00,
        )
        self.sale_history_data = {
            "autosalon": self.autosalon.id,
            "supplier": self.supplier.id,
            "price": 25000.00,
        }

    def test_sale_history_list(self):
        response = self.client.get(path=reverse(viewname="histories-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistorySerializer(
            [
                self.first_sale_history,
                self.second_sale_history,
                self.third_sale_history,
            ],
            many=True,
        ).data
        serializer_prices = [item.get("price") for item in serializer_data]
        response_prices = [item.get("price") for item in response.data]

        self.assertListEqual(response_prices, serializer_prices)

    def test_sale_history_create(self):
        response = self.client.post(
            path=reverse(viewname="histories-list"), data=self.sale_history_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_sale_history_retrieve(self):
        response = self.client.get(
            path=reverse(viewname="histories-detail", args=[self.first_sale_history.id])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SaleHistorySerializer(self.first_sale_history).data
        serializer_price = serializer_data.get("price")
        response_price = response.data.get("price")

        self.assertEqual(response_price, serializer_price)

    def test_sale_history_update(self):
        response = self.client.put(
            path=reverse(
                viewname="histories-detail", args=[self.second_sale_history.id]
            ),
            data=self.sale_history_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        sale_history = SaleHistory.objects.get(price=25000.00)
        self.assertEqual(sale_history.price, 25000.00)

    def test_sale_history_destroy(self):
        response = self.client.delete(
            path=reverse(viewname="histories-detail", args=[self.third_sale_history.id])
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(SaleHistory.objects.filter(price=35000.00).exists())


class SpecialOfferOfAutoSalonTestCase(APITestCase):
    """
    APITestCase for SpecialOfferOfAutoSalonViewSet
    """

    def setUp(self):
        self.first_autosalon = G(
            model=AutoSalon, name="WestCoastCustoms", location="US", balance=100000.00
        )
        self.second_autosalon = G(
            model=AutoSalon, name="AutoHouse", location="US", balance=10000.00
        )

        self.first_special_offer_of_autosalon = G(
            model=SpecialOfferOfAutoSalon,
            name="Sale 20%",
            descr="Special offer for customers!",
            discount=2000,
            dealer=self.first_autosalon,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.second_special_offer_of_autosalon = G(
            model=SpecialOfferOfAutoSalon,
            name="Sale 30%",
            descr="Special offer for customers!",
            discount=5000,
            dealer=self.second_autosalon,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.third_special_offer_of_autosalon = G(
            model=SpecialOfferOfAutoSalon,
            name="Sale 60%",
            descr="Special offer for customers!",
            discount=25000,
            dealer=self.second_autosalon,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.special_offer_of_autosalon_data = {
            "name": "Sale 70%",
            "descr": "Special offer for autosalons!",
            "discount": 2000,
            "dealer": self.first_autosalon.id,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=7),
        }

    def test_special_offer_of_autosalon_list(self):
        response = self.client.get(path=reverse(viewname="offers_autosalon-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SpecialOfferOfAutoSalonSerializer(
            [
                self.first_special_offer_of_autosalon,
                self.second_special_offer_of_autosalon,
                self.third_special_offer_of_autosalon,
            ],
            many=True,
        ).data
        serializer_names = [item.get("name") for item in serializer_data]
        response_names = [item.get("name") for item in response.data]

        self.assertListEqual(response_names, serializer_names)

    def test_special_offer_of_autosalon_create(self):
        response = self.client.post(
            reverse("offers_autosalon-list"), data=self.special_offer_of_autosalon_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_special_offer_of_autosalon_retrieve(self):
        response = self.client.get(
            path=reverse(
                viewname="offers_autosalon-detail",
                args=[self.first_special_offer_of_autosalon.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SpecialOfferOfAutoSalonSerializer(
            self.first_special_offer_of_autosalon
        ).data
        serializer_name = serializer_data.get("name")
        response_name = response.data.get("name")

        self.assertEqual(response_name, serializer_name)

    def test_special_offer_of_autosalon_update(self):
        response = self.client.put(
            path=reverse(
                viewname="offers_autosalon-detail",
                args=[self.second_special_offer_of_autosalon.id],
            ),
            data=self.special_offer_of_autosalon_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        special_offer = SpecialOfferOfAutoSalon.objects.get(name="Sale 70%")
        self.assertEqual(special_offer.name, "Sale 70%")

    def test_special_offer_of_autosalon_destroy(self):
        response = self.client.delete(
            path=reverse(
                viewname="offers_autosalon-detail",
                args=[self.third_special_offer_of_autosalon.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            SpecialOfferOfAutoSalon.objects.filter(name="Sale 60%").exists()
        )


class SpecialOfferOfSupplierTestCase(APITestCase):
    """
    APITestCase for SpecialOfferOfSupplierViewSet
    """

    def setUp(self):
        self.first_supplier = G(
            model=Supplier,
            name="AutoHouse",
            year_of_issue=timezone.now(),
            price=25000.00,
        )
        self.second_supplier = G(
            model=Supplier,
            name="Atlant-M",
            year_of_issue=timezone.now(),
            price=15000.00,
        )

        self.first_special_offer_of_supplier = G(
            model=SpecialOfferOfSupplier,
            id=1,
            name="Sale 20%",
            descr="Special offer for autosalons!",
            discount=2000,
            supplier=self.first_supplier,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.second_special_offer_of_supplier = G(
            model=SpecialOfferOfSupplier,
            id=2,
            name="Sale 30%",
            descr="Special offer for autosalons!",
            discount=5000,
            supplier=self.second_supplier,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.third_special_offer_of_supplier = G(
            model=SpecialOfferOfSupplier,
            id=3,
            name="Sale 60%",
            descr="Special offer for suppliers!",
            discount=25000,
            supplier=self.first_supplier,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )
        self.special_offer_of_supplier_data = {
            "name": "Sale 70%",
            "descr": "Special offer for autosalons!",
            "discount": 2000,
            "supplier": self.second_supplier.id,
            "start_date": timezone.now(),
            "end_date": timezone.now() + timedelta(days=7),
        }

    def test_special_offer_of_supplier_list(self):
        response = self.client.get(path=reverse(viewname="offers_customer-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = SpecialOfferOfSupplierSerializer(
            [
                self.first_special_offer_of_supplier,
                self.second_special_offer_of_supplier,
                self.third_special_offer_of_supplier,
            ],
            many=True,
        ).data
        serializer_names = [item.get("name") for item in serializer_data]
        response_names = [item.get("name") for item in response.data]

        self.assertListEqual(response_names, serializer_names)

    def test_special_offer_of_supplier_create(self):
        response = self.client.post(
            reverse("offers_customer-list"), data=self.special_offer_of_supplier_data
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_special_offer_of_supplier_retrieve(self):
        response = self.client.get(
            path=reverse(
                viewname="offers_customer-detail",
                args=[self.second_special_offer_of_supplier.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer_data = SpecialOfferOfSupplierSerializer(
            self.second_special_offer_of_supplier
        ).data
        serializer_name = serializer_data.get("name")
        response_name = response.data.get("name")

        self.assertEqual(response_name, serializer_name)

    def test_special_offer_of_supplier_update(self):
        response = self.client.put(
            path=reverse(
                viewname="offers_customer-detail",
                args=[self.second_special_offer_of_supplier.id],
            ),
            data=self.special_offer_of_supplier_data,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        special_offer = SpecialOfferOfSupplier.objects.get(name="Sale 70%")
        self.assertEqual(special_offer.name, "Sale 70%")

    def test_special_offer_of_supplier_destroy(self):
        response = self.client.delete(
            path=reverse(
                viewname="offers_customer-detail",
                args=[self.third_special_offer_of_supplier.id],
            )
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(
            SpecialOfferOfSupplier.objects.filter(name="Sale 60%").exists()
        )
