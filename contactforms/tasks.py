from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .email import send_email_function, send_own_email_function
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name='send_email_task')
def send_email_task(fname, email, body, lname, company):
    return send_email_function(fname, email, body, lname, company)


@shared_task(name='send_own_email_task')
def send_own_email_task(fname, email, body, lname, company):
    return send_own_email_function(fname, email, body, lname, company)