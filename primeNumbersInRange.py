start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

for num in range(start, end + 1):
    if num > 1:  # primes are > 1
        for i in range(2, int(num**0.5) + 1):  # check divisors
            if num % i == 0:
                break   # divisor found → stop checking
        else:
            print(num)  # only runs if no divisor was found
