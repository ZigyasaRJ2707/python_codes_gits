def puzzle(W, N): 
    new = ""
    for i in range(len(W)): 
        if (i + 1) % N == 0: 
            new = new + "_"
        else: 
            new = new + W[i]
    return new

print(puzzle("television", 2))