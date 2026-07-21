import pickle

f = open("student.dat", "rb")

name = input("Enter student name: ")

found = False

try:
    while True:
        record = pickle.load(f)

        if record == name:
            print(record)
            found = True
            break

except EOFError:
    f.close()

if not found:
    print("Record not found")