-- populate data for business database
USE oscarbooks;

INSERT INTO vendors VALUES
(NULL, 100, "4gsm", "Watson", "2022-04-28", "2020-06-15"),
(NULL, 101, "New Shelves Books", "Austin", "2022-05-30", "2020-07-07"),
(NULL, 102, "Bella Distribution", "Gable", "2022-05-20", "2020-06-30");

INSERT INTO vendoremail VALUES
(NULL, 1, "purchases@4gsm.com"),
(NULL, 2, "orders@nsbooks.com"),
(NULL, 3, "purchases@belladistribution.com");


INSERT INTO vendorphone VALUES
(NULL, 1, "415-239-8864"),
(NULL, 2, "971-279-5741"),
(NULL, 3, "865-262-0204 ");

INSERT INTO vendoraddress VALUES
(NULL, 1, "58 Middle Point Rd", "San Francisco", "California", "94124", "US"),
(NULL, 2, "9938 SE Old Town Ct", "Happy Valley", "Oregon", "97086", "US"),
(NULL, 3, "403 E Andrew Johnson Hwy", "Jefferson City", "Tennesse", "37760", "US");

INSERT INTO customers VALUES
(NULL, "Jimmy", "Cole", "Obrien"),
(NULL, "Jake", "Isaiah", "Storialle"),
(NULL, "Zack", "Finn", "Prizeman");

INSERT INTO customeraddress VALUES
(NULL, 1, "514 Grandview Ave", "Yakima", "Washington", "98144", "US"),
(NULL, 2, "912 Grending Ave", "Richland", "Washington", "98136", "US"),
(NULL, 3, "184 Washington St", "Prosser", "Washington", "98158", "US");


INSERT INTO customeremail VALUES
(NULL, 1, "yanks4444life@yahoo.com"),
(NULL, 2, "metsmeansbest@gmail.com"),
(NULL, 3, "5ox4ever@gmail.com");


INSERT INTO customerphone VALUES
(NULL, 1, "509-903-5768"),
(NULL, 2, "509-903-0819"),
(NULL, 3, "206-840-9119");

INSERT INTO employees VALUES
(NULL, 121, "Adam", "Tyler", "Cole", "Operations Manager", "2020-06-10", "full", 1),
(NULL, 138, "Claudio", "Cesaro", "Castagnoli", "Stock Associate", "2020-06-10", "part", 0),
(NULL, 252, "Karen", "Jennay", "Fukihara", "Floor Manager", "2020-06-10", "full", 1),
(NULL, 303, "Manny", NULL, "Ramirez", "Cashier", "2022-03-06", "part", 0),
(NULL, 336, "Adam", "Matthew", "Page", "Stock Associate", "2021-08-04", "casual", 0),
(NULL, 451, "Rhea", "Brianne", "Rodriguez", "Cashier", "2020-06-10", "full", 0),
(NULL, 120, "Nyla", "Mary", "Hale", "Cashier", "2021-11-23", "part", 0);

INSERT INTO employeeaddress VALUES
(NULL, 1, "2441 13th Ave SW", "Seattle", "Washington", "98106", "US"),
(NULL, 2, "9514 8th Ave S", "Seattle", "Washington", "98108", "US"),
(NULL, 3, "9668 Rainier Ave S", "Seattle", "Washington", "98118", "US"),
(NULL, 4, "679 46th Ave SW", "Seattle", "Washington", "98136", "US"),
(NULL, 5, "9816 51st Ave", "Seattle", "Washington", "98136", "US"),
(NULL, 6, "924 13th Ave NE", "Seattle", "Washington", "98146", "US"),
(NULL, 7, "156 13th Ave", "Seattle", "Washington", "98118", "US");


INSERT INTO employeephone VALUES
(NULL, 1, "206-721-8558"),
(NULL, 2, "206-789-0682"),
(NULL, 3, "206-721-1022"),
(NULL, 4, "206-937-1068"),
(NULL, 5, "206-937-0127"),
(NULL, 6, "206-956-3116"),
(NULL, 7, "206-936-4397");


INSERT INTO employeeemail VALUES
(NULL, 1, "adam.cole80@gmail.com"),
(NULL, 2, "claudiol28@gmail.com"),
(NULL, 3, "karen_fukihara@yahoo.com"),
(NULL, 4, "manny.ramirez@hotmail.com"),
(NULL, 5, "adam_page@yahoo.com"),
(NULL, 6, "rhearodriguez@gmail.com"),
(NULL, 7, "nyla316@gmail.com");

INSERT INTO products VALUES
(NULL, "Mythematics", "book"),
(NULL, "The Lost Civilization Enigma", "book"),
(NULL, "Fundamentals of Musical Acoustics", "book"),
(NULL, "Ideas - Notebook", "notebook"),
(NULL, "Light writing color pens - pack of 3", "writing utensil"),
(NULL, "Much Love writing pad", "stationary"),
(NULL, "Think Freely writing pad", "stationary");

INSERT INTO inventory VALUES
(NULL, 1, 13, 15.99),
(NULL, 2, 10, 24.99),
(NULL, 3, 6, 29.99),
(NULL, 4, 4, 9.99),
(NULL, 5, 25, 5.99),
(NULL, 6, 24, 7.99),
(NULL, 7, 23, 7.99);

INSERT INTO purchasetransactions VALUES
(NULL, 1, 54, 3, "2022-01-15", 675.86),
(NULL, 2, 55, 3, "2022-01-27", 844.44),
(NULL, 3, 56, 3, "2022-01-27", 119.84);

INSERT INTO purchasetransactionitem VALUES
(NULL, 1, 1, 11.99, 24, 156.81),
(NULL, 1, 2, 18.75, 24, 206.68),
(NULL, 1, 3, 22.49, 16, 278.17),
(NULL, 2, 5, 4.49, 60, DEFAULT),
(NULL, 2, 6, 5.99, 48, DEFAULT),
(NULL, 2, 7, 5.99, 48, DEFAULT),
(NULL, 3, 4, 7.49, 16, DEFAULT);

INSERT INTO salestransactions VALUES
(NULL, 1, 3, "2022-04-12", 666.41),
(NULL, 2, 6, "2022-04-18", 49.93),
(NULL, 1, 7, "2022-04-25", 409.62),
(NULL, 3, 4, "2022-05-01", 268.98),
(NULL, 2, 6, "2022-04-10", 85.93),
(NULL, 2, 4, "2022-04-16", 64.95);

INSERT INTO salestransactionitem VALUES
(NULL, 1, 1, 15.99, 5, DEFAULT),
(NULL, 1, 2, 24.99, 5, DEFAULT),
(NULL, 1, 3, 29.99, 5, DEFAULT),
(NULL, 1, 5, 5.99, 20, DEFAULT),
(NULL, 1, 6, 7.99, 12, DEFAULT),
(NULL, 1, 7, 7.99, 12, DEFAULT),
(NULL, 2, 4, 9.99, 2, DEFAULT),
(NULL, 2, 5, 5.99, 5, DEFAULT),
(NULL, 3, 1, 15.99, 3, DEFAULT),
(NULL, 3, 2, 24.99, 6, DEFAULT),
(NULL, 3, 3, 29.99, 2, DEFAULT),
(NULL, 3, 5, 5.99, 4, DEFAULT),
(NULL, 3, 6, 7.99, 8, DEFAULT),
(NULL, 3, 7, 7.99, 8, DEFAULT),
(NULL, 4, 1, 19.99, 2, DEFAULT),
(NULL, 4, 2, 24.99, 2, DEFAULT),
(NULL, 4, 3, 29.99, 2, DEFAULT),
(NULL, 4, 4, 9.99, 4, DEFAULT),
(NULL, 4, 5, 5.99, 4, DEFAULT),
(NULL, 4, 6, 7.99, 4, DEFAULT),
(NULL, 4, 7, 7.99, 4, DEFAULT),
(NULL, 5, 1, 19.99, 1, DEFAULT),
(NULL, 5, 3, 29.99, 1, DEFAULT),
(NULL, 5, 4, 9.99, 2, DEFAULT),
(NULL, 5, 5, 5.99, 2, DEFAULT),
(NULL, 5, 7, 7.99, 1, DEFAULT),
(NULL, 6, 2, 24.99, 1, DEFAULT),
(NULL, 6, 4, 9.99, 4, DEFAULT);