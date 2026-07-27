import pickle 

def display(): 
    n = int(input("enter the number of items:"))
    f = open("items.dat", "wb")
    for i in range(n): 
        item = int(input("enter item number: "))
        item_name = input("enter item name: ")
        quantity = int(input("enter quantity of said item: "))
        price = float(input("enter price of item: "))
        rec = (item, item_name, quantity, price)
        pickle.dump(rec, f)
    f.close()

    f = open("items.dat", "rb")

    try: 
        while True: 
            rec = pickle.load(f)
            print("item no: ", rec[0])
            print("item name: ", rec[1])
            print("quantity: ", rec[2])
            print("price: ", rec[3])
            print("amount: ", rec[2] * rec[3])
    except EOFError: 
        f.close()
