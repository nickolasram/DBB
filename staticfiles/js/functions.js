function construct_join(){
    return 0
}

function construct_query(dat, col, tab, joins){
    database = dat;
    column = col;
    tables = tab;
    join_clause = joins;
    basic_query = `SELECT ${column}
    FROM ${tables}
    ${joins};`
    return basic_query
}

function changeDB(){
    console.log(document.getElementById("databaseDropdown").value);
}
function changeTable(){
    console.log(document.getElementById("tableDropdown").value);
}
function changeOrder(){
    console.log(document.getElementById("orderDropdown").value);
}
function orderSwitch(){
    if (document.getElementById("orderBtn").innerHTML== "Asc"){
        document.getElementById("orderBtn").innerHTML= "Desc";
    } else {
        document.getElementById("orderBtn").innerHTML= "Asc";
    }
}
function searchDatabase(){
    console.log(document.getElementById("searchDB").value);
}

function expandFilter(){
    let height = $("#tableOptionsDiv").outerHeight()*1.5;
    $("#expandBtn").click(function(){
        $("#tableOptionsDiv").slideToggle(height);
    })
}

function toggleWrap(){
    $("#wrapBtn").click(function() {
        $(".data-cell").each(function(){
            $(this).toggleClass("unwrappedcell wrappedcell");
        });
    });
}

function insertQuery(){
    let exampleNumber = $("#exampleQueries").val();
    if (exampleNumber == "defaultText"){
        $('#queryArea').empty();
    } else{
        $.get(`static/queries/${exampleNumber}.txt`, function(data) {
            $('#queryArea').html(data);
         }, 'text');
    }
}

function buildSimpleQuery(table){
    let query = `
     SELECT *
     FROM ${table};
    `
    return query
}

function returnRecJoins(table){
    $.ajax({
        url: "/joins/",
        method: "POST",
        data: {
            tableNumber: table,
            },
        datatype: "json",
        success: function(data){
            $('#placeForJoinFilter').html($(data));
            getJoinSelection();
            returnColumns('POST');
        }
    })
}

function returnSelectedTable(){
    $('#tableBtn').click(function(e){
        e.preventDefault();
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: buildSimpleQuery($('input[name="tableSelection"]:checked').val()),
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
                returnRecJoins($('input[name="tableSelection"]:checked').attr('data-table-number'));
                console.log($('input[name="tableSelection"]:checked').val());
            }
        })
    })
}


function runQuery(){
    $('#queryBtn').click(function(e){
        e.preventDefault();
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: $('#queryArea').val(),
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
            }
        })
    })
};


function runGetJoins(){
    $.ajax({
        url: "/joins/",
        method: "GET",
        success: function(data){
            $('#placeForJoinFilter').html($(data));
            returnColumns('POST');
        }
    })
}


function runGetQuery(){
    $.ajax({
        url: "/results/",
        method: "GET",
        success: function(data){
            $('#placeForResults').html($(data).html());
            runGetJoins();
        }
    })
};

function returnColumns(method){
    if (method == 'GET'){
        $.ajax({
            url: "/columns/",
            method: "GET",
            success: function(data){
                $('#placeForColumnFilter').html($(data));
                getColumnSelection();
            }
        })
    }
    else{
        $.ajax({
            url: "/columns/",
            method: "POST",
            data: {
                query: $('input[name="tableSelection"]:checked').val(),
            },
            success: function(data){
                $('#placeForColumnFilter').html($(data));
                getColumnSelection();
            }
        })
    }
}

function getColumnSelection(){
    $('#testColumnBtn').click(function(){
        let columns = [];
        $(".columnOption").each(function(){
            if ($(this).is(':checked')){
                columns.push($(this).val())
            }
        });
        let colString = columns.join(",");
        let joins = [];
        $(".joinOption").each(function(){
            if ($(this).is(':checked')){
                joins.push($(this).attr('data-join'))
            }
        });
        let joinsString = joins.join("\n");
        tab = $('input[name="tableSelection"]:checked').val()
        let query = construct_query('placeholder database', colString, tab, joinsString);
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: query,
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
            }
        })
    })
}


function getJoinSelection(){
    $('#joinBtn').click(function(){
        let joins = [];
        $(".joinOption").each(function(){
            if ($(this).is(':checked')){
                joins.push($(this).attr('data-join'))
            }
        });
        let joinsString = joins.join("\n");
        // test section
        tab = $('input[name="tableSelection"]:checked').val()
        let query = construct_query('placeholder database', '*', tab, joinsString);
        console.log(query);
        $.ajax({
            url: "/results/",
            method: "POST",
            data: {
                query: query,
                },
            datatype: "json",
            success: function(data){
                $('#placeForResults').html($(data).html());
            }
        })
    })
}


$(document).ready(function(){
    runGetQuery()
    setTimeout(function(){
        $("#tableOptionsDiv").slideUp(0);
        toggleWrap();
        returnColumns('GET');
        runQuery();
        getJoinSelection();
        getColumnSelection();
        returnSelectedTable();
        expandFilter()
    }, 533);
});