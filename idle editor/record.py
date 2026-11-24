import pickle

f = open("record.dat", "wb")

employees = [
    [1, "Aman", 25000],
    [2, "Riya", 30000],
    [3, "Kabir", 28000]
]

pickle.dump(employees, f)
f.close()
