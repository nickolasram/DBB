import datetime
from decimal import Decimal
import json
from datetime import date


class DecimalDateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    if isinstance(obj, datetime.date):
      return str(obj)
    if isinstance(obj, set):
      return str(obj)
    return json.JSONEncoder.default(self, obj)
