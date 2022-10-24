from .mysqlhelp import dataBase
from .mysqlhelp import retrieve_value, store_value
import json


def fetch_schemas():
    key = "schemas"
    cache_check = retrieve_value(key, 5)
    if cache_check:
        return json.loads(cache_check)
    cursorObject = dataBase.cursor(buffered=True, dictionary=True)
    cursorObject.execute("SHOW SCHEMAS;")
    query_set = cursorObject.fetchall()
    defaults = ['information_schema', 'sys', 'performance_schema', 'mysql', 'DBBRDSDB']
    results = []
    for x in query_set:
        if x['Database'] not in defaults:
            results.append(x['Database'])
    store_value(key, json.dumps(results), 5)
    return results