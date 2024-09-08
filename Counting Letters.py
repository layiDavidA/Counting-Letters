# Count the frequency of letters appearing in a string \list

def freqletters():
    sentence = input("Enter sentence\t")
    sentence = sentence.lower()
    sentence = list(sentence)
    d = {}

    for i in sentence:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i]+1
    print(d)


freqletters()
