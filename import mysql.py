import mysql.connector

print("start")

con = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    use_pure=True,
    connection_timeout=3
)

print(con.is_connected())