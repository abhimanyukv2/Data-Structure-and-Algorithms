'''Write a Python program that inputs a list of words, separated by white-
space, and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
'''

def cleanUpText(sentence):   
    sentence = sentence.lower()
    unwantedCharecters = {'\n', '.', '!', "'", '?', ','}
    for char in unwantedCharecters:
        sentence = sentence.replace(char, ' ')
    return sentence

def wordOccurance(sentence):
    sentence = cleanUpText(sentence)
    occurance = {}
    for word in sentence:
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1
    return occurance

sentence = input()
ans = wordOccurance(sentence)
print(ans)