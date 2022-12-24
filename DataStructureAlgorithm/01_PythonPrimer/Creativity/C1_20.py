'''Python’s random module includes a function shuffle(data) that accepts a list of elements and randomly reorders the elements so that each possible order occurs with equal probability. The random module includes a more basic function randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint function, implement your own version of the shuffle function.'''

import random

def ownShuffleFunction(data):
    ownShuffel = []
    numberOfItteration = 0
    index = [x for x in range(len(data))]
    while True:
        number = random.randint(0, len(data)-1)
        # print('number: ',number)
        if number in index:
            ownShuffel.append(data[number])
            index.remove(number)
        
        if len(index) == 0:
            break
            
        numberOfItteration += 1
    
        # print('ownShuffel: ',ownShuffel)
        # print('index: ',index)
    print('number of itteration:',numberOfItteration)
    
    return ownShuffel

data = list(map(int, input().split()))
ans = ownShuffleFunction(data)
print(list(ans))
random.shuffle(data)
print(data)