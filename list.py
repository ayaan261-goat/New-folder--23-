def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] ==[-1]:
            ctr += 1
            lst.append(word)

        print("same\n",lst)
    
count = match_words(['abc','cfc','xyz','aba', '1221'])
print("hello:"),count
