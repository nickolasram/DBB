function construct_query(col, tab, joins, order){
    let column = col;
    let tables = tab;
    let join_clause = joins;
    let basic_query = `SELECT ${column}
    FROM ${tables}
    ${joins}
    ${order};`
    return basic_query
}

function filter_search(){
    $('#searchForm').submit(function(e){
        e.preventDefault();
        let column = constructColumnsString();
        let table = $('input[name="tableSelection"]:checked').val();
        let joins = constructJoinsString();
        let filter = $('#searchDB').val()
        let filterColumns = []
        $(".columnOption").each(function(){
            if ($(this).is(':checked')){
                filterColumns.push($(this).val())
            }
        });
        let filterString = filterColumns.join(` LIKE "%${filter}%"\nOR `);
        filterString += ` LIKE "%${filter}%"`
        let selection = $('#orderDropdown').val();
        let order = `ORDER BY ${selection} ${$('#orderBtn').data('order')}`;
        let query = `SELECT ${column}
        FROM ${table}
        ${joins}
        WHERE ${filterString}
        ${order};`
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: query,
                schema: $('#databaseDropdown').val()
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
            }
        })
    })
}

function constructJoinsString(){
    let joins = [];
    $(".joinOption").each(function(){
        if ($(this).is(':checked')){
            joins.push($(this).attr('data-join'))
        }
    });
    let joinsString = joins.join("\n");
    return joinsString;
}

function constructColumnsString(){
    let columns = [];
    $(".columnOption").each(function(){
        if ($(this).is(':checked')){
            columns.push($(this).val())
        }
    });
    let colString = columns.join(", ");
    return colString;
}

function collapseFilters(){
    let fList = ["table", "join", "column"];
    for (let i in fList){
        $(`.filterList[data-filter="${fList[i]}"]`).slideUp(0);
    }
}

function expandFilter(){
    $(".filter-button").each(function(){
        $(this).click(function(){
            console.log("expanding")
            let filter=$(this).data('filter');
            let statusSpan = $(`.expandStatus[data-filter="${filter}"]`);
            let filterDiv = $(`.filterList[data-filter="${filter}"]`);
            let height = filterDiv.outerHeight()*1.5;
            filterDiv.slideToggle(height);
            if (statusSpan.text() == 'Expand'){
                statusSpan.text("Collapse");
                $(`p[data-filter="${filter}"]`).hide();
            } else{
                statusSpan.text("Expand");
                $(`p[data-filter="${filter}"]`).show();
            }
        })
    })
}

function toggleWrap(){
    $("#wrapBtn").click(function() {
        $(".data-cell").each(function(){
            $(this).toggleClass("unwrappedcell wrappedcell");
        });
    });
}

function buildSimpleQuery(table){
    let query = `
     SELECT *
     FROM ${table};
    `
    return query
}

function changeOrderColumn(){
    $('#orderDropdown').change(function(){
        getOrderSelection();
    })
}

function changeOrderDirection(){
    $('#orderBtn').click(function(){
        if  ($(this).data('order') == 'ASC'){
            $(this).data('order', 'DESC')
            $(this).html('DESC')
        } else{
            $(this).data('order', 'ASC')
            $(this).html('ASC')
        }
        getOrderSelection();
    })
}

function getOrderSelection(){
    selection = $('#orderDropdown').val();
    orderClause = `ORDER BY ${selection} ${$('#orderBtn').data('order')}`;
    let colString = constructColumnsString();
    let joinsString = constructJoinsString();
    tab = $('input[name="tableSelection"]:checked').val()
    let query = construct_query(colString, tab, joinsString, orderClause);
    $.ajax({
        url: "/results/",
        method: "POST",
        data: {
            query: query,
            schema: $('#databaseDropdown').val()
            },
        datatype: "json",
        success: function(data){
            $('#placeForResults').html($(data).html());
        }
    })
}

function returnOrderDropdown(method, callCase){
    if (method == 'GET'){
        return $.ajax({
            url: "/order/",
            method: "GET"
        })
    }
    else{
        switch (callCase){
            case 'tableChange':
                return $.ajax({
                    url: "/order/",
                    method: "POST",
                    data: {
                        table: $('input[name="tableSelection"]:checked').val(),
                        schema: $('#databaseDropdown').val(),
                        joining: false
                    }
                })
                break;
            case 'schemaChange':
                return $.ajax({
                    url: "/order/",
                    method: "POST",
                    data: {
                        table: false,
                        schema: $('#databaseDropdown').val(),
                        joining: false
                    }
                })
                break;
            case 'joinsChange':
                return $.ajax({
                    url: "/order/",
                    method: "POST",
                    data: {
                        table: $('input[name="tableSelection"]:checked').val(),
                        schema: $('#databaseDropdown').val(),
                        joins: constructJoinsString(),
                        joining: true
                    }
                })
                break;
        }
    }
}

function postReturnOrderDropdown(data){
    $('#orderForm').html($(data));
    changeOrderColumn();
    changeOrderDirection();
}

function returnJoins(method, table){
    if (method == 'GET'){
        return $.ajax({
            url: "/joins/",
            method: "GET"
        })
    } else{
        return $.ajax({
            url: "/joins/",
            method: "POST",
            data: {
                tableNumber: table,
                schema: $('#databaseDropdown').val()
                },
            datatype: "json"
        })
    }
}

function postReturnJoins(method, data){
    $('#placeForJoinFilter').html($(data));
    let returnColumnsData = returnColumns();
    returnColumnsData.done(function(data){
        postReturnColumns(data);
    });
    if (method == 'POST'){
        getJoinSelection();
        $(`.filterList[data-filter="join"]`).slideUp(0);
        $(`.expandStatus[data-filter="join"]`).text("Expand");
    }
}

function returnSelectedTable(){
    $('#tableBtn').click(function(e){
        e.preventDefault();
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: buildSimpleQuery($('input[name="tableSelection"]:checked').val()),
                schema: $('#databaseDropdown').val()
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
                let returnOrderDropdownData = returnOrderDropdown('POST', 'tableChange');
                returnOrderDropdownData.done(function(data){
                    postReturnOrderDropdown(data);
                    let returnJoinsData = returnJoins('POST', $('input[name="tableSelection"]:checked').attr('data-table-number'));
                    returnJoinsData.done(function(data){
                        postReturnJoins('POST', data);
                    });
                });
            }
        })
    })
}

function changeExampleQuery(){
    $('#exampleQueries').change(function(){
        $('.qDatabaseOption').each(function(){
            if  ($(this).val() == $('.exampleQueryOption:selected').attr('data-eSchema')){
                $(this).prop('selected', true);
            } else {
                $(this).prop('selected', false);
            }
        })
        $('#queryArea').val($('#exampleQueries').val());
    })
}

function runQuery(){
    $('#queryForm').submit(function(e){
        e.preventDefault();
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: $('#queryArea').val(),
                schema: $('#queryDatabaseDropdown').val(),
                source: 'user'
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
            }
        })
    })
};

function returnSchemaTables(){
    return $.ajax({
        url: "/tables/",
        method: "POST",
        data: {
                schema: $('#databaseDropdown').val()
                }
    })
}

function returnBasicQuery(method){
    if (method == 'GET'){
        return $.ajax({
            url: "/results/",
            method: "GET"
        })
    }
    else {
        return $.ajax({
        url: "/results/",
        method: "POST",
        data: {
                query: buildSimpleQuery($('input[name="tableSelection"]:checked').val()),
                schema: $('#databaseDropdown').val()
                }
        })
    }
};

function returnColumns(){
    return $.ajax({
        url: "/columns/",
        method: "POST",
        data: {
            table: $('input[name="tableSelection"]:checked').val(),
            schema: $('#databaseDropdown').val(),
            joining: false
        }
    })
}

function postReturnColumns(data){
    $('#placeForColumnFilter').html($(data));
    getColumnSelection();
    columnChangeOrder();
    $(`.filterList[data-filter="column"]`).slideUp(0);
    $(`.expandStatus[data-filter="column"]`).text("Expand");
}

function getColumnSelection(){
    $('#testColumnBtn').click(function(){
        let colString = constructColumnsString();
        let joinsString = constructJoinsString();
        tab = $('input[name="tableSelection"]:checked').val()
        let query = construct_query(colString, tab, joinsString, '');
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: query,
                schema: $('#databaseDropdown').val()
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
            }
        })
    })
}

function returnJoinedColumns(listOfJoins, schema, table){
    $.ajax({
        url: "/columns/",
        method: "POST",
        data: {
            schema: schema,
            joining: true,
            joins: listOfJoins,
            table: table
            },
        datatype: "json",
        success: function(data){
            postReturnColumns(data);
            let returnOrderDropdownData = returnOrderDropdown('POST', 'joinsChange');
            returnOrderDropdownData.done(function(data){
                postReturnOrderDropdown(data);
            });
        }
   })
}

function getJoinSelection(){
    $('#joinBtn').click(function(){
        let joinsString = constructJoinsString();
        tab = $('input[name="tableSelection"]:checked').val()
        let query = construct_query('*', tab, joinsString, '');
        let schema = $('#databaseDropdown').val();
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: query,
                schema: schema
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
                returnJoinedColumns(joinsString, schema, tab);
            }
        })
    })
}


function changeSchema(){
    $('#databaseDropdown').change(function(){
        let returnSchemaTablesData = returnSchemaTables();
        returnSchemaTablesData.done(function(data){
            $('#placeForTableFilter').html($(data));
            let returnBasicQueryData = returnBasicQuery('POST');
            returnBasicQueryData.done(function(data){
                $('#placeForResults').html($(data).html());
                let returnOrderDropdownData = returnOrderDropdown('POST', 'schemaChange');
                returnOrderDropdownData.done(function(data){
                    postReturnOrderDropdown(data);
                    let returnJoinsData = returnJoins('POST', 0);
                    returnJoinsData.done(function(data){
                        postReturnJoins('POST', data);
                        returnSelectedTable();
                        $(`.filterList[data-filter="table"]`).slideUp(0);
                        $(`.expandStatus[data-filter="table"]`).text("Expand");
                    });
                });
            });
        });
    })
}

function columnChangeOrder(){
    $('.columnOption').change(function(){
        let orderOption = $(`option[value=${$(this).val()}]`)
        if ($(this).is(':checked')){
           orderOption.show()
        } else{
           orderOption.hide()
        }
    })
}

$(document).ready(function(){
    let returnSchemaTablesData = returnSchemaTables();
    returnSchemaTablesData.done(function(data){
        $('#placeForTableFilter').html($(data));
        let returnBasicQueryData = returnBasicQuery('GET');
        returnBasicQueryData.done(function(data){
            $('#placeForResults').html($(data).html());
            let returnOrderDropdownData = returnOrderDropdown('GET', null);
            returnOrderDropdownData.done(function(data){
                postReturnOrderDropdown(data);
                let returnJoinsData = returnJoins('GET', null);
                returnJoinsData.done(function(data){
                    postReturnJoins('GET', data);
                    changeSchema();
                    toggleWrap();
                    filter_search();
                    runQuery();
                    getJoinSelection();
                    returnSelectedTable();
                    expandFilter();
                    changeExampleQuery();
                    collapseFilters();
                });
            });
        });
    });
});