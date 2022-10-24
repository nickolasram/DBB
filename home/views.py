from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .schemas import fetch_schemas
from .mysqlhelp import *
import json
from .flush import flush_cache
from .decimalEncoder import DecimalDateEncoder

def home(request):
    database_list = fetch_schemas()
    examples = example_queries()
    context = {'schemas': database_list,
               'examples': examples}
    return render(request, 'home/home.html', context)


@csrf_exempt
def results(request):
    cursorObject = dataBase.cursor(buffered=True, dictionary=True)
    state = 'success or table failure'
    if request.method == 'POST':
        cursorObject.execute(f"USE {request.POST['schema']};")
        query = request.POST["query"]
    else:
        query = default_query('oscarbooks')
        cursorObject.execute("USE oscarbooks;")
    cache_check = retrieve_value(query, 7)
    if cache_check:
        result = json.loads(cache_check)
    else:
        try:
            cursorObject.execute(query)
        except:
            if request.POST['source'] == 'user':
                state = 'user error'
            query = default_query(request.POST['schema'])
            cursorObject.execute(f"USE {request.POST['schema']};")
            cursorObject.execute(query)
        result = cursorObject.fetchall()
        store_value(query, json.dumps(result, cls=DecimalDateEncoder), 7)
    context = {'results': result,
               'state': state}
    return render(request, 'home/results.html', context)


@csrf_exempt
def joins(request):
    if request.method == 'POST':
        table_numb = int(request.POST["tableNumber"])
        schema = request.POST["schema"]
        status = "expanded"
    else:
        table_numb = 0
        schema = 'oscarbooks'
        status = "collapsed"
    table_names = get_table_names(schema)
    foreign_constraints = f_constraints(schema, table_names[table_numb])
    related_columns = return_right_result(foreign_constraints)
    if (related_columns):
        column = related_columns[0]
    else:
        column = None
    context = {'table_numb': table_numb,
               'table': table_names[table_numb],
               'column': column,
               'results': results,
               'related_columns': related_columns,
               'status': status}
    return render(request, 'home/joins.html', context)


@csrf_exempt
def columns(request):
    if request.method == 'POST':
        status = "expanded"
    else:
        status = "collapsed"
    context = {'columns': ultimate_column_retrieval(request),
               'status': status}
    return render(request, 'home/columns.html', context)


@csrf_exempt
def tables(request):
    schema = request.POST['schema']
    table_names = get_table_names(schema)
    context = {'tables': table_names}
    return render(request, 'home/tables.html', context)


@csrf_exempt
def order(request):
    context = {'columns': ultimate_column_retrieval(request)}
    return render(request, 'home/order.html', context)


def flush(request):
    flush_cache()
    return render(request, 'home/flushed.html')
