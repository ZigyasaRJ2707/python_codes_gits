stack = []
while True:
     ch = int(input('''1. Push,
            2. Pop,
            3. Display,
            4. Exit
            '''))
     if ch == 1:
        n = int(input("enter how many books to be recorded: "))
        for i in range(n):
            book = input("enter book name: ")
            copies = int(input("enter number of copies: "))
            cost = int(input("enter cost of book: "))
            data = [book, copies, cost]
            stack.append(data)
        print("added")

     elif ch == 2:
        if len(stack) != 0:
            print("removed: ", stack.pop())
        else:
            print("stack is empty")
     elif ch == 3:
        for record in reversed(stack):
            print(record)
     elif ch == 4:
        print("bye bye!")
        break

    
        
        
