from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbb.settings')
BROKER_CONNECTION_RETRY = True
BROKER_CONNECTION_MAX_RETRIES = 0
app = Celery('dbb', broker=f'redis://:{os.environ["REDIS_PW"]}@localhost:6379/0')
app.config_from_object('django.conf:settings', namespace='Celery')
app.autodiscover_tasks()