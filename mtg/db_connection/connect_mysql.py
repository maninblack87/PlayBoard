import mysql.connector

# MySQL로 DB연결
def connect_to_mysql():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "maninblack87*",
        database = "mtg"
    )