import pickle
f = open("School.dat", "wb")
schools = [
    [101, "Greenwood School", 250],
    [102, "Sunrise Public School", 150],
    [103, "Riverdale Academy", 200],
    [104, "Hillview School", 320]
]
pickle.dump(schools, f)
f.close()
f = open("School.dat", "rb")
records = pickle.load(f)
for i in records:
    if i[2] > 200:
        print(i)
f.close()
