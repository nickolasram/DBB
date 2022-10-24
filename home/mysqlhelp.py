import mysql.connector
import difflib
import json
import os
import datetime
import redis
from .decimalEncoder import DecimalDateEncoder
from .flush import pw as rpw

DIRNAME = os.path.dirname(__file__)
cache_file = os.path.join(DIRNAME, 'cache.json')

DB_HOST = os.environ['DBB_DB_HOST']
DB_USER = os.environ['DBB_DB_USER']
DB_PW = os.environ['DBB_DB_PW']
DBU_HOST = os.environ['DBB_DBU_HOST']
DBU_USER = os.environ['DBB_DBU_USER']
DBU_PW = os.environ['DBB_DBU_PW']

dataBase = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PW,
    connection_timeout=10,
)

dataBaseUnlimited = mysql.connector.connect(
    host=DBU_HOST,
    user=DBU_USER,
    passwd=DBU_PW,
    connection_timeout=10,
)

def store_value(key, value, db_ind):
    client = redis.Redis(host='localhost', port=6379, password=rpw, db=db_ind)
    client.set(key, value)
    client.expire(key, datetime.timedelta(days=3))


def retrieve_value(key, db_ind):
    client = redis.Redis(host='localhost', port=6379, password=rpw, db=db_ind)
    value = client.get(key)
    return value


def order_by(column, direction):
    return f"ORDER BY {column} {direction};"


def get_table_names(schema):
    key = schema
    cache_check = retrieve_value(key, 4)
    if cache_check:
        return json.loads(cache_check)
    table_cursor = dataBase.cursor(buffered=True, dictionary=True)
    table_cursor.execute(f"USE {schema};")
    table_cursor.execute("SHOW FULL TABLES;")
    tables = table_cursor.fetchall()
    defaults = ['auth_group', 'auth_group_permissions', 'auth_permission', 'auth_user', 'auth_user_groups',
                'auth_user_user_permissions', 'django_admin_log', 'django_content_type', 'django_migrations', 'django_session']
    names = []
    for i in tables:
        if i["Tables_in_"+schema] not in defaults and i['Table_type'] == "BASE TABLE":
            names.append(i["Tables_in_"+schema])
    store_value(key, json.dumps(names, cls=DecimalDateEncoder), 4)
    return names


def get_column_names(table, schema):
    key = schema + table
    cache_check = retrieve_value(key, 3)
    if cache_check:
        return json.loads(cache_check)
    column_cursor = dataBase.cursor(buffered=True, dictionary=True)
    column_cursor.execute(f"USE {schema};")
    column_cursor.execute(f"DESC {table};")
    columns = column_cursor.fetchall()
    columns_formatted = []
    for i in columns:
        columns_formatted.append(i['Field'])
    store_value(key, json.dumps(columns_formatted, cls=DecimalDateEncoder), 3)
    return columns_formatted


def get_joined_column_names(table, schema, joins):
    key = schema + table
    cache_check = retrieve_value(key, 2)
    if cache_check:
        return json.loads(cache_check)
    join_column_cursor = dataBaseUnlimited.cursor(buffered=True, dictionary=True)
    join_column_cursor.execute(f"USE {schema};")
    view_constructor = f'''CREATE VIEW jointable AS
                            SELECT * FROM {table}
                            {joins};'''
    join_column_cursor.execute(view_constructor)
    join_column_cursor.execute('DESC jointable;')
    query_set = join_column_cursor.fetchall()
    join_column_cursor.execute("DROP VIEW jointable;")
    results = []
    for column_data in query_set:
       results.append(column_data['Field'])
    store_value(key, json.dumps(results, cls=DecimalDateEncoder), 2)
    return results


def ultimate_column_retrieval(request):
    if request.method == 'POST':
        if request.POST["table"] != 'false':
            table = request.POST["table"]
        else:
            table = get_table_names(request.POST["schema"])[0]
        if request.POST["joining"] == 'true':
            columns = get_joined_column_names(table, request.POST["schema"], request.POST["joins"])
        else:
            columns = get_column_names(table, request.POST["schema"])
    else:
        table_numb = 0
        table_names = get_table_names('oscarbooks')
        columns = get_column_names(table_names[table_numb], 'oscarbooks')
    return columns


def f_constraints(schema, table):
    key = schema + table
    cache_check = retrieve_value(key, 1)
    if cache_check:
        return json.loads(cache_check)
    query = f'''
    WITH just_tables AS (
        SELECT TABLE_NAME, REFERENCED_TABLE_NAME
        FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS
        WHERE CONSTRAINT_SCHEMA = '{schema}'),
    table_key AS (
    	SELECT
        TABLE_NAME,COLUMN_NAME
        FROM
        INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE
        CONSTRAINT_SCHEMA = '{schema}'
        AND
        (REFERENCED_TABLE_NAME = '{table}'
        OR TABLE_NAME = '{table}'))
    SELECT DISTINCT *
    FROM table_key
    JOIN just_tables
    USING(TABLE_NAME)
    WHERE TABLE_NAME = '{table}'
    OR REFERENCED_TABLE_NAME = '{table}';
    '''
    f_cursor = dataBase.cursor(buffered=True, dictionary=True)
    f_cursor.execute(f"USE {schema};")
    f_cursor.execute(query)
    results = f_cursor.fetchall()
    store_value(key, json.dumps(results, cls=DecimalDateEncoder), 1)
    return results


def return_right_result(list):
    key = "".join(list[0].values())
    cache_check = retrieve_value(key, 6)
    if cache_check:
        return json.loads(cache_check)
    ref = 'TABLE_NAME'
    col = 'COLUMN_NAME'
    comp = 'REFERENCED_TABLE_NAME'
    checked = set()
    result = []
    for i in list:
        signature = (i[ref], i[comp])
        if signature not in checked:
            checked.add(signature)
            queue = []
            for j in list:
                if i[ref] == j[ref] and i[comp] == j[comp]:
                    queue.append(j[col])
                if i[ref] == j[comp] and {ref: i[ref], col: i[col], comp: j[ref]} not in result:
                    result.append({ref: i[ref], col: i[col], comp: j[ref]})
            closest_match = difflib.get_close_matches(i[comp], queue, 1, 0)
            if {ref: i[comp], col: closest_match[0], comp: i[ref]} not in result:
                result.append({ref: i[ref], col: closest_match[0], comp: i[comp]})
    store_value(key, json.dumps(result, cls=DecimalDateEncoder), 6)
    return result


def default_query(schema):
    table_names = get_table_names(schema)
    columns = get_column_names(table_names[0], schema)
    order = order_by(columns[0], "ASC")
    query = f"SELECT * FROM {table_names[0]} {order}"
    return query


def example_queries():
    with open(cache_file, 'r') as cache:
        cache_data = json.load(cache)
        queries = cache_data["example_queries"]
        return queries