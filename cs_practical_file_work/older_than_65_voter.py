import csv
f = open("VOTER.CSV", "r")
records = csv.reader(f)
for i in records:
    if int(i[2]) > 65:
        print(i)
f.close()
