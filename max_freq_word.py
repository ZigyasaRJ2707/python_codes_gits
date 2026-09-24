f = open("anthem.txt", "r")
content =  f.read().lower()
words = content.split()

freq = {} 
for word in words: 
    if word in freq: 
        freq[word] +=1
    else: 
        freq[word] = 1
max_count = 0 
max_word = ""

for word in freq: 
    print(word, ":", freq[word])  
    if word[freq] > max_count:
        max_count = freq[word]
        max_word = word
print("maximum frequency word: ", max_word)
print("frequency: ", max_count)    
