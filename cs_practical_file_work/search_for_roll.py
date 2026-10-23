import pickle
f = open("students.dat", "wb")
record = [[1, "Aman"], [2, "Riya"], [3, "Chunaid Khan"], [4, "Sharkie"]]
pickle.dump(record, f)
f.close()

f = open("students.dat", "rb")
roll = int(input("enter roll number to search for: "))
try:
    while True:
        record = pickle.load(f)
        for i in record:
            if i[0] == roll:
                print("record found: ", i)
                break
        else:
                print("roll number not found")
except EOFError:
    pass
f.close()
