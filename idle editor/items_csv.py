import csv
f = open("items.csv", "w", newline="")
w = csv.writer(f)
data = []
n = int(input("enter number of items to be registered:"))

for i in range(n):
    code = input("enter item code: ")
    desc = input("enter item desc: ")
    price = input("enter item price:")

    data.append([code, desc, price])
w.writerow(["code", "description", "price"])

w.writerows(data)

f.close()
print("\nCode\tDescription\tPrice")
for row in data:
    print(row[0], "\t", row[1], "\t", row[2])
