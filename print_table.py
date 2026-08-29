import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    use_pure=True
)

cur = con.cursor()

cur.execute("use student;")

sql = "insert into students values(%s, %s, %s, %s, %s, %s, %s)"
data = [
    (107, "Ziggy", "Hyd", 343, 99, "A", "ziggydonut@gamil.com"),
    (117, "Sam", "Delhi", 17, 99, "A", "samisaloser@gmail.com"),
    (180, "Neil", "Pune", 18, 99, "A", "neilurneil@gmail.com")
]
cur.executemany(sql, data)
con.commit()
print("inserted!")
cur.execute("select * from students")
for row in cur:
    print(row)

con.close()