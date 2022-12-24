'''Write a short Python function that takes a string s, representing a sentence, and returns a copy of the string with all punctuation removed. For example, if given the string "Let's try, Mike.", this function would return "Lets try Mike".'''

import string

def deletePunctuation(s):
    st = list(s)
    punctuation = list(string.punctuation)
    # print(punctuation)
    for i in st:
        if i in punctuation:
            st.remove(i)
    # print(st)
    withoutPunctuation = ''
    for i in st:
        withoutPunctuation += i
    return withoutPunctuation

s = input()
ans = deletePunctuation(s)
print(ans)