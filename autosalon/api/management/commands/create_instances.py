from django.core.management.base import BaseCommand
from api.models import AutoSalon, Car, OptionCar, Supplier
from faker import Faker


class Command(BaseCommand):
    """
    Custom command for create AutoSalon, Car, OptionCar, Supplier instances
    """

    help = "Create base instances"

    def handle(self, *args, **options):
        faker = Faker()

        # Populate AutoSalon
        for _ in range(3):
            AutoSalon.objects.create(
                name=faker.unique.company(),
                location=faker.country(),
                balance=faker.pydecimal(8, min_value=100000.00, positive=True),
            )

        # Populate Car
        for _ in range(4):
            Car.objects.create(
                model_name=faker.random_element(
                    elements=(
                        "BMW M5 F90 CS",
                        "AUDI RS7 PERFORMANCE",
                        "MERCEDES-BENZ AMG GT 4-Door Coupe",
                        "Porsche Panamera Executive",
                    )
                ),
            )

        # Populate OptionCar
        for _ in range(4):
            OptionCar.objects.create(
                year=faker.date(),
                mileage=faker.random_number(digits=4),
                body_type=faker.random_element(elements=("sedan",)),
                transmission_type=faker.random_element(elements=("automatic",)),
                drive_unit_type=faker.random_element(elements=("complete",)),
                color=faker.random_element(elements=("red", "blue", "green", "black")),
                engine_type=faker.random_element(elements=("petrol",)),
            )

        # Populate Supplier
        for _ in range(5):
            Supplier.objects.create(
                name=faker.unique.company(),
                year_of_issue=faker.date(),
                price=faker.pydecimal(8, min_value=10000.00, positive=True),
            )

        self.stdout.write(self.style.SUCCESS("Data populated successfully"))
