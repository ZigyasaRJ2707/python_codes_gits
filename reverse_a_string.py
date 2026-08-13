def reverse(str):
    rev = "" 
    for i in range(len(str)-1, -1, -1):
        if str[i]!= " ": 
            rev = rev + str[i]
    l = len(rev)
    tup = (rev, l) 
    return tup 
print(reverse("hello there"))
