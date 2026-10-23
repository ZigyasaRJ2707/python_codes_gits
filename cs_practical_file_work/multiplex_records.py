import pickle
f= open("MULTIPLEX.DAT", "wb")
n = int(input("enter the number of multiplexes to be put in the list: "))
records = []
for i in range(n):
    Mno = int(input("enter multiplex number: "))
    Mname = input("enter multiplex name: ")
    Type = input("enter type: ")
    records.append([Mno, Mname, Type])
pickle.dump(records,f)
f.close()

f = open("MULTIPLEX.DAT", "rb")
records = pickle.load(f)
f.close()

remaining = []
for j in records:
    if j[1][0]!= "S":
        remaining.append(j)
f = open("MULTIPLEX.DAT", "wb")
pickle.dump(remaining, f)
f.close()
print(remaining)
