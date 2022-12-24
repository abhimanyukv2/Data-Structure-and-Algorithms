'''Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).'''

def distinctNumber(sequence):
    distinct = []
    for i in sequence:
        if i in distinct:
            return '{} is repeated.'.format(i)
        else:
            distinct.append(i)
    
    return 'all number are distinct in sequence'

sequence = list(map(int, input().split()))
ans = distinctNumber(sequence)
print(ans)