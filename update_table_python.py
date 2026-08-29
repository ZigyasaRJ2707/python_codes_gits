import mysql.connector

con = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    use_pure=True
)

cur = con.cursor()

cur.execute("use student;")
sql = "UPDATE students SET marks = %s WHERE roll_no = %s"
data = (100, 108)

cur.execute(sql, data)
con.commit()

print("Updated!")
cur.execute("SELECT * FROM students")
print(cur.fetchall())