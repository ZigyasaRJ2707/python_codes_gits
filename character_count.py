def char_count(str, char): 
    count = 0 
    for ch in str:
        if ch == char:  
            count+=1 
    return count 

str = input("enter any statement: ")
char = input("enter the character to be counted: ") 
count = char_count(str, char)
print(f"the character '{char}' occurs in the statement '{str}' {count} number of times. ")