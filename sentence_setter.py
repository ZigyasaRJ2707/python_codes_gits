def sentence_setter():
    with open("STORY.txt", "r") as f: 
        content = f.read()
        sentence = ""
        for i in content:
            sentence+=i 
            if i in "?!.": 
                print(sentence.strip())
                sentence = ""
sentence_setter()     

