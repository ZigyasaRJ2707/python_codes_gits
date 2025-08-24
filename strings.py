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


n = int(input("enter any number: "))
ans = get_sum_of_digits(n)
print(ans) 




