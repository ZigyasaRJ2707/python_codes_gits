def replace_vowels(s): 
    vowels_list = "aeiouAEIOU" 
    for i in s: 
        for j in vowels_list: 
            if i == j: 
                s = s.replace(i, "*")   # ✅ assign back here
    return s 

s = "hello!"
print(replace_vowels(s))