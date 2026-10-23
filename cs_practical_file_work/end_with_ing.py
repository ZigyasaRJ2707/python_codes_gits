def end_with_ing():
    f = open("SAMPLE.txt", "r")
    text = f.read()
    words = text.split()
    count = 0
    for word in words:
        if word[-3:] == "ing":
            count+=1
    f.close()
    return count
print(end_with_ing())
        
