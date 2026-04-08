def is_prime(n): 
    if n<2: 
        return False 
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0: 
            return False 
    else: 
        return True 
total = 0 
for k in range(1, 1000): 
    if is_prime(k) and is_prime(k+2):
         print(k, k+2)
         total+=1 
         if total==5:
             break

