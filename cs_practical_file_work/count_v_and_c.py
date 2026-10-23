def count_v_and_c():
    f = open("SAMPLE.txt", "r")
    text = f.read()
    vowels = 0
    consonants = 0
    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou":
                vowels+=1
            else:
                consonants+=1
    return "vowels: ", vowels, "consonants: ", consonants
    f.close()

print(count_v_and_c())
