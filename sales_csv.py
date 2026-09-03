import csv

def accept():
    f = open("Sales.csv", "a", newline="")
    w = csv.writer(f)

    n = int(input("Enter number of records: "))

    for i in range(n):
        pid = input("Product ID: ")
        pname = input("Product Name: ")
        qty = int(input("Quantity Sold: "))
        price = int(input("Price Per Unit: "))

        w.writerow([pid, pname, qty, price])

    f.close()

def calculate():
    f = open("Sales.csv", "r", newline="")
    r = csv.reader(f)
    total = 0
    for row in r:
        total = total + int(row[2]) * int(row[3])

    f.close()
    return total

def display():
    f = open("Sales.csv", "r", newline="")
    r = csv.reader(f)

    print("\nProduct_ID\tProduct_name\tQuantity_sold\tPrice_per_unit\tTotal")
    for row in r:
        print(row[0], "\t", row[1], "\t", row[2], "\t", row[3])
    f.close()
accept()
display()
print("Total Sales =", calculate())
