import mysql.connector

print("Before")

db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    connect_timeout=5
)

print("After")
db.close()