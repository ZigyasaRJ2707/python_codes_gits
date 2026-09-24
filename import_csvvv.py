import csv
f = open("sports.csv", "w", newline="")
w = csv.writer(f, delimiter = "\t")
n = int(input("enter no. of records: "))

for i in range(n):
    sport = input("enter sport:")
    competition = input("enter competition: ")
    prize = input("enter prize won: ")
    w.writerow([sport, competition, prize])
f.close()
print("records stored")

f = open("sports.csv", "r")
r = csv.reader(f, delimiter="\t")

print("\nSports Records:")

for row in r:
    print(row)

f.close()