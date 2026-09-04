import pickle 
def update_data():
    f = open("record.dat", "rb")
    g = open("temp.dat", "wb")
    employees = pickle.load(f)
    x = int(input("enter employee ID: "))
    found = False 
    for i in employees:
        if i[0] == x: 
            i[2] = int(input("enter new salary of employee: "))
            found = True
    if not found: 
            print("employee not found")
    pickle.dump(employees, g)
    f.close()
    g.close()
update_data()