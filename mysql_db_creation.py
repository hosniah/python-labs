import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'm2i_python_db'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha database
cursor.execute("CREATE DATABASE m2i_python_db")