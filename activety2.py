

def match_words(words):
    ctr = 0
    Ist = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            Ist.append(word)
        
        print("list of words with first and last character same\n", Ist)
        return ctr
    
count = match_words(['abc', 'cfc','xyz', 'aba', '1221'])
print("number of words having first and last character same:", count)