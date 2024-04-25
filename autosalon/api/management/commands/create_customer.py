from django.core.management.base import BaseCommand
from users.models import Customer
from faker import Faker


class Command(BaseCommand):
    """
    Custom command for create Customer instances
    """

    help = "Create customer base instances"

    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(3):
            Customer.objects.create(
                username=faker.random_element(
                    elements=("admin", "manager", "customer")
                ),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.unique.email(),
                password=faker.password(),
                balance=faker.pydecimal(8, min_value=10000.00, positive=True),
            )

        self.stdout.write(self.style.SUCCESS("Customer data populated successfully"))
