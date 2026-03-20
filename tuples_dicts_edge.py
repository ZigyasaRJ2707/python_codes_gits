t = (1, [2, 3])
t[1].append(4) # we can modify a LIST INSIDE a tuple, because LISTS are mutable. nice edge case
print(t) 

''' d = {}
d[([1, 2], 3)] = "hello"   (this code gives an error, because dicts can only have hashable keys. Lists are MUTABLE
but dict keys must be IMMUTABLE to be HASHABLE) ''' 


