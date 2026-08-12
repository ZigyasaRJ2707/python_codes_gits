def lenWords(str): 
    L = []
    for word in str.split():
        num = len(word) 
        L.append(num)
    T = tuple(L)
    return T 

print(lenWords("this is so much fun yay"))