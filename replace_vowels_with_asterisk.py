def replace_vowels(s): 
    vowel_list = "aeiouAEIOU" 
    for v in vowel_list: 
        s = s.replace(v, "*")
    return s 
print(replace_vowels("Hellloooooo!"))