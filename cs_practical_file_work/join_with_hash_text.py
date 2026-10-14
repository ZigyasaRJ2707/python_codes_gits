import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("sample.txt", "r")
for line in f: 
    words = line.split()
    print("#".join(words))

