# %%
def if_palindrome(n):
    s = str(n)

    l = len(s)

    for i in range(0, l//2): 
        if s[i] != s[l-i-1]:
            return 0

    return 1 

def get_sum_of_digits(n): 
    sum = 0 
    while n>0: 
        last_digit = n%10 # find out last digit of number
        sum+=last_digit # add last digit to sum
        n = n//10 # truncate the last digit since it's already added
    return sum 


def get_prime_numbers(lower_limit, upper_limit):

    for i in range(lower_limit, upper_limit+1): 
        isPrime = 1 
        for j in range(2, int(i**0.5+1)): 
            if i%j == 0: 
                # i is composite 
                isPrime = 0 
                #print(f"{j} divides {i}, let's go to next i ")
            continue  
        if isPrime: 
            print(f"{i} is prime") 
            

n1 = 2
n2 = 50
get_prime_numbers(n1, n2)
# n = int(input("enter any number: "))
# ans = get_sum_of_digits(n)
# print(ans) 





# %%
