from random import randint
def generate(n): 
    return randint(10**(n-1), (10**n) - 1)

print(generate(3))
print(generate(3))
print(generate(3))
