## importing 'mysql.connector' as mysql for convenient
## pip install mysql-connector-python

import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

print(db) # it will print a connection object if everything is fine