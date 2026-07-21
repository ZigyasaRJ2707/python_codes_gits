import pickle

f = open("student.dat", "rb")

try:
    while True:
        record = pickle.load(f)
        print(record)

except EOFError:
    f.close()