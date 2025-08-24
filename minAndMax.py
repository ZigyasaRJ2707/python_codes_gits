num_list = []

for i in range(5): 
     num = float(input(f"Enter number {i+1}: "))
     num_list.append(num)

print(min(num_list))
print(max(num_list))
