'''def puzzles(W, N):
    new = ""
    for i in range(len(W)):
        if (i+1)%N == 0:
            new = new + "_"
        else:
            new = new + W[i]
    return new

print(puzzles("whoexcitedforpryme", 4))'''

'''def sentence_setter():
    with open("STORY.txt", "r") as f:
        content = f.read()
        sentence = ""
        for i in content:
            sentence+=i
            if i in "?!.":
                print(sentence.strip())
                sentence = ""
sentence_setter() '''

'''import pickle
def update_records():
    f = open("emp.dat", "ab")
    n = int(input("enter how many employees to be appended: "))
    for i in range(n):
        employee_id = int(input("enter employee id:"))
        employee_name = input("enter employee name: ")
        dept = input("enter department: ")
        sal = int(input("enter salary: "))
        records = [employee_id, employee_name, dept, sal]
        pickle.dump(records, f)
    print("employee records updated successfully")
    f.close()

def update_salary():
    f = open("emp.dat", "rb")
    new_list = []
    while True:
        employee = pickle.load(f)
        if employee[2] == "IT": 
            employee[3] = 200000
        new_list.append(employee)
    print("salaries updated.")
    with open("emp.dat", "wb") as f:
        for employee in new_list:
            pickle.dump(employee, f)'''

import pickle 
def copy_new():
    try:
        f = open("items.dat", "rb")
        g = open("new_items.dat", "ab")
        records = pickle.load(f)
        for item_id, list in records:
            if list[1] > 1000:
                pickle.dump({item_id: list}, g)
    except EOFError:
        break
        f.close()
        g.close()
        



