f = open("ITEM.CSV", "r")
records = csv.reader(f)
for i in records:
    print(i[0])
    totalPrice = int(i[1]) * float(i[2])
    print(totalPrice)
f.close()
