def sum_of_digits():
    total = 0
    n = int(input("enter the number: "))
    while n>0: 
        digit = n%10
        total+=digit
        n = n//10
    print(total)
sum_of_digits()
