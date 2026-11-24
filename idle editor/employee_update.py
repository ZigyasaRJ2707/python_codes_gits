import pickle

employees = [
    [1, "Aman", 25000],
    [2, "Riya", 30000],
    [3, "Kabir", 28000]
]

f = open("record.dat", "wb")
pickle.dump(employees, f)
f.close()

print("record.dat created!")
