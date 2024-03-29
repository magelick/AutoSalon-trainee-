from celery import Celery
import os

# set default settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autosalon.settings")
# initial Celery instance
app = Celery("autosalon")
# setting config objects from settings
app.config_from_object("django.conf:settings", namespace="CELERY")
# auto discover for tasks
app.autodiscover_tasks()
