from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .mysqlhelp import *
from .schemas import *


@shared_task(name='pingDb')
def pingDb():
    table_cursor = dataBase.cursor(buffered=True, dictionary=True)
    table_cursor.execute("USE musicrating;")