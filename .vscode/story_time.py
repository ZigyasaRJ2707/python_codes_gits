f = open("story.txt", "r")
text = f.read()
sentence = ""

for i in text: 
    sentence+=i
    if i in "!.?":
        print(sentence.strip())
        sentence = ""

f.close()