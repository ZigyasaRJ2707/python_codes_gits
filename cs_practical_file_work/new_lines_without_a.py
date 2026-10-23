def remove_a():
    f = open("sample.txt", "r")
    g = open("new.txt", "w")
    text = f.readlines()
    for line in text:
        if "a" not in line:
            g.write(line)
    g.close()
    g = open("new.txt", "r")
    new_text = g.readlines()
    for i in new_text:
        print(i)
    g.close()
    f.close()

remove_a()
