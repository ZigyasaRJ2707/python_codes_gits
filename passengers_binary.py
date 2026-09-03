import pickle 

def create(): 
    f = open("passengers.dat", "wb")
    n = int(input("how many passengers?: "))
    passengers = [] 
    for i in range(n):
        pnr = input("enter passenger number: ")
        pname = input("enter passenger name: ")
        brdstn = input("enter boarding station name: ")
        destn = input("enter your destination: ")
        far = float(input("enter fare: "))
        passengers.append([pnr, pname, brdstn, destn, far])
    pickle.dump(passengers, f)
    f.close()

def search(): 
    f = open("passengers.dat", "rb")
    d = input("enter the destination: ")
    passengers = pickle.load(f)
    for i in passengers: 
        if i[3] == d: 
            print("records found.")
            print(i)
            found = True
    if not found: 
            print("no records found")
    f.close()

def update_fare():
    f = open("passengers.dat", "rb+")
    passengers = pickle.load(f)
    for i in passengers: 
         i[4] = i[4] * 1.05
    f.seek(0)
    pickle.dump(passengers, f)
    f.close()

create()
update_fare()
search()
