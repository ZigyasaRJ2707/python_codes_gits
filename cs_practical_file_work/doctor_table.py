import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    use_pure = True,
    database = "hospital"
    )
cur = con.cursor()

while True:
    print("\n1. Insert a new doctor")
    print("2. Delete doctors with fees above 300")
    print("3. Increase fees by 200 where experience exceeds 10")
    print("4. Display female doctors")
    print("5. Display all doctors")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sql = "insert into doctor values (%s, %s, %s, %s, %s, %s)"
        doc_id = int(input("enter ID: "))
        name = input("enter name: ")
        field = input("enter expertise field of doctor: ")
        gen = input("Enter M for male, F for female: ")
        exp = int(input("enter experience years: "))
        fee = int(input("enter fee of doctor: "))
        data = [doc_id, name, field, gen, exp, fee]
        cur.execute(sql, data)
        con.commit()
        cur.execute("select * from doctor")
        for row in cur.fetchall():
            print(row)
    elif choice == 2:
        cur.execute("delete from doctor where fees > 300")
        con.commit()
        print("records deleted")
    elif choice == 3:
        cur.execute("update doctor set fees = fees + 200 where experience > 10")
        con.commit()
        print("print fees updated")
    elif choice == 4:
        cur.execute("select * from doctor where sex = 'F' ")
        for row in cur.fetchall():
            print(row)
    elif choice == 5:
        cur.execute("select * from doctor")
        for row in cur.fetchall():
            print(row)
    elif choice == 6:
        print("Bye bye!")
        break
    else:
        print("please enter a valid option")
cur.close()
con.close()















        

