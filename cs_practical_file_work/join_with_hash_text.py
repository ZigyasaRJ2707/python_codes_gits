f = open("SAMPLE.txt", "r")
for line in f: 
    words = line.split()
    print("#".join(words))
    
