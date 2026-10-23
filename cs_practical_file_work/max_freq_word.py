def most_freq_word():
    f = open("SAMPLE.txt", "r")
    text = f.read()
    words = text.split()
    d = {}
    for word in words:
        if word in d:
            d[word]+=1
        else:
            d[word] = 1
    max_count = max(d.values())
    for word in d:
        if d[word] == max_count:
            print("word with most frequency: ", word, max_count)

    f.close()
most_freq_word()
