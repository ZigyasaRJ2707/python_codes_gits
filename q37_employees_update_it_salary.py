import pickle 
with open("employees.dat", "ab") as f:
    n = int(input("how many employees to be entered?: "))
    for i in range(n) : 
        id = input("enter employee id: ")
        name = input("enter employee name: ")
        dept = input("enter employee department:")
        salary = int(input("enter salary: "))
        pickle.dump([id, name, dept, salary], f)  #to update employee records 
    print("employees added")
def update_data():
    f = open("employees.dat", "rb")
    g = open("temp.dat", "wb")
    while True: 
        try: 
            employees = pickle.load(f)
            if employees[2] == "IT":
                   employees[3] = 200000
            pickle.dump(employees, g)
        except EOFError: 
            break 
    f.close()
    g.close()