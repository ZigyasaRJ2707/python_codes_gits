def LShift(Arr, n): 
    for i in range(n):
        x = Arr.pop(0)
        Arr.append(x)
    return Arr
print(LShift([10, 20, 30, 40, 50], 3))
