import pickle

# ---------- Store Records ----------

f = open("student.dat", "wb")

for i in range(3):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))

    record = [name, marks]
    pickle.dump(record, f)

f.close()

# ---------- Search Record ----------

f = open("student.dat", "rb")

name = input("Enter student name to search: ")

found = False

try:
    while True:
        record = pickle.load(f)

        if record[0] == name:
            print(record)
            found = True
            break

except EOFError:
    f.close()

if not found:
    print("Record not found")