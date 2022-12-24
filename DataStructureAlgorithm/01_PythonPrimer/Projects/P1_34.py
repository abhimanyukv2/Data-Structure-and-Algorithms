'''A common punishment for school children is to write out a sentence mul-
tiple times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.'''

import random

sentence = "I will never spam my friends again."

randomIndex = []
while len(randomIndex) < 8:
    num = random.randint(0,100)
    if num not in randomIndex:
        randomIndex.append(num)
print(randomIndex)
# randomIndex.sort()

for i in range(1,101):
    if i in randomIndex:
        randomPosition = random.randint(0,len(sentence)-1)
        randomAlphabet = random.randint(ord('a'), ord('z'))
        print(i, sentence[:randomPosition]+chr(randomAlphabet)+sentence[randomPosition+1:], '<- This is typo')
    else:
        print(i, sentence)