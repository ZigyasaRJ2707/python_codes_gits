def remove_lowercase():
    f = open("infile.txt", "r")
    g = open("outfile.txt", "w")
    for line in f:
        if not line[0].islower():
            g.write(line)
    f.close()
    g.close()
remove_lowercase()
