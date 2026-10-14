def palindrome(n):
    for i in range(len(n)):
        if n[i] != n[len(n) - i - 1]:
            return "NOT a palindrome"
        return "palindrome"
print(palindrome("civic"))