def divisible_by_five(nums):
    total = 0
    for i in nums: 
        if i % 5 == 0: 
            total+=i
    return total
print(divisible_by_five([20, 30, 5, 23, 43]))

