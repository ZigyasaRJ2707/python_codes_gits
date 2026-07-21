import pickle

f = open("student.dat", "wb")

for i in range(3):
    name = input("Enter name: ")
    pickle.dump(name, f)

f.close()