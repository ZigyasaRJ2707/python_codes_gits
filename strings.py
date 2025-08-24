# %%
def if_palindrome(n):
    s = str(n)

    l = len(s)

    for i in range(0, l//2): 
        if s[i] != s[l-i-1]:
            return 0

    return 1 

n = 727 
ans = if_palindrome(n)
print(ans)
# %%
