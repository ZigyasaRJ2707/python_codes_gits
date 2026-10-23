import pickle

f = open("students.dat", "wb")
record = [[1, "Aman", 75], [2, "Riya", 90], [3, "Chunaid Khan", 89], [4, "Sharkie", 67]]
pickle.dump(record, f)
f.close()

f = open("students.dat", "rb")
roll = int(input("enter roll number to search for: "))

try:
    while True:
        record = pickle.load(f)
        for i in record:
            if i[0] == roll:
                i[2]+=10
                print(i)
                break
        else:
            print("roll number not found")
except EOFError:
    pass

f.close()
f = open("students.dat", "wb")
pickle.dump(record, f)
f.close()
