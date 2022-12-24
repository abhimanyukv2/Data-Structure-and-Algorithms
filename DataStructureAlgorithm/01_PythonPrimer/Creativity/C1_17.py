'''Had we implemented the scale function (page 25) as follows, does it work properly?

def scale(data, factor):
    for val in data:
        val *= factor

Explain why or why not'''

def scale(data, factor):
    for val in data:
        val *= factor

data = list(map(int,input().split()))
factor = int(input())
scale(data, factor)
print(data)

'''This wouldn't have worked. val is an alias to the actual element in data and assigning a new object to it will only change val's value.'''