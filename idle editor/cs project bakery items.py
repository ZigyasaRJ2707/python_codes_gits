import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bakery",
    use_pure = True
)

cur = con.cursor()


def create():
    try:
        sql = """
            create table bakery_items (
                item_id int primary key,
                item_name varchar(50),
                price int,
                quantity int
            )
        """
        cur.execute(sql)
        print("Table created successfully!")

    except mysql.connector.Error as error:
        print("Database error:", error)


def insert():
    try:
        n = int(input("How many items do you want to add? "))

        for i in range(n):

            item_id = int(input("Enter item ID: "))
            name = input("Enter item name: ")
            price = int(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            sql = "insert into bakery_items values (%s, %s, %s, %s)"
            data = (item_id, name, price, quantity)

            cur.execute(sql, data)
            con.commit()

            print("Item added successfully!")

    except ValueError:
        print("Please enter numbers for ID, price and quantity.")

    except mysql.connector.Error as error:
        print("Database error:", error)


def display():
    try:
        print("1. All item details")
        print("2. Item names and prices")
        print("3. Item names and quantities")
        print("4. Items below a certain price")

        ch = input("Enter your choice: ")

        if ch == "1":
            sql = "select * from bakery_items"
            cur.execute(sql)

        elif ch == "2":
            sql = "select item_name, price from bakery_items"
            cur.execute(sql)

        elif ch == "3":
            sql = "select item_name, quantity from bakery_items"
            cur.execute(sql)

        elif ch == "4":
            price = float(input("Enter the price limit: "))

            sql = "select * from bakery_items where price < %s"
            data = (price,)

            cur.execute(sql, data)

        else:
            print("Invalid choice.")
            return

        records = cur.fetchall()

        if not records:
            print("No items found.")
        else:
            for row in records:
                print(row)

    except ValueError:
        print("Please enter a number for the price.")

    except mysql.connector.Error as error:
        print("Database error:", error)


try:
    n = int(input("How many times do you want to use the menu? "))

    for i in range(n):
        print("1. Create table")
        print("2. Insert items")
        print("3. Display items")
        print("4. Exit")

        ch = input("Enter your choice: ")

        if ch == "1":
            create()

        elif ch == "2":
            insert()

        elif ch == "3":
            display()

        elif ch == "4":
            print("Goodbye!")
            break

        else:
            print("Please choose 1, 2, 3 or 4.")

except ValueError:
    print("Please enter a whole number for the menu repetitions.")

cur.close()
con.close()
