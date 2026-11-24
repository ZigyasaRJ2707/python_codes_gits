'''def puzzles(W, N):
    new = ""
    for i in range(len(W)):
        if (i+1)%N == 0:
            new = new + "_"
        else:
            new = new + W[i]
    return new

print(puzzles("whoexcitedforpryme", 4))'''

'''def sentence_setter():
    with open("STORY.txt", "r") as f:
        content = f.read()
        sentence = ""
        for i in content:
            sentence+=i
            if i in "?!.":
                print(sentence.strip())
                sentence = ""
sentence_setter() '''



