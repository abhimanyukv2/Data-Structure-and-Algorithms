'''Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing.'''

def myReverse1(data):
    reverse = []
    for i in range(len(data)-1, -1, -1):
        reverse.append(data[i])
    return reverse

def myReverse2(data):
    return [data[i] for i in range(len(data)-1, -1, -1)]

def myReverse3(data):
    return data[::-1]

data = list(map(int, input().split()))
ans1 = myReverse1(data)
print(ans1)
ans2 = myReverse1(data)
print(ans2)
ans3 = myReverse1(data)
print(ans3)


def pythonReverse(data):
    return reversed(data)

data1 = list(map(int,input().split()))
ans4 = pythonReverse(data1)
print(list(ans4))