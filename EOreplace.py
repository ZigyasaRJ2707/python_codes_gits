def EOReplace(L): 
    for i in range(len(L)): 
        if L[i]%2 == 0: 
            L[i]+=1
        else:
            L[i]-=1
    return L

print(EOReplace([10, 23, 24, 26, 88]))           