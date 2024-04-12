from __future__ import absolute_import, unicode_literals

from celery import Celery
import os
from celery.schedules import crontab
from django.apps import apps

# set default settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autosalon.settings")
# initial Celery instance
app = Celery("autosalon")
# setting config objects from settings
app.config_from_object("django.conf:settings", namespace="CELERY")
# auto discover for tasks
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])

app.conf.beat_schedule = {
    "deal_between_autosalon_and_supplier": {
        "task": "api.tasks.buy_car_between_autosalon_and_supplier",
        "schedule": crontab(minute="*/10"),
        "args": (1, 1),
    },
    "deal_between_customer_and_autosalon": {
        "task": "api.tasks.buy_car_between_customer_and_autosalon",
        "schedule": crontab(minute="*/15"),
        "args": (1, 1, 50000, "BMW M5 G30"),
    },
}
