'''Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution'''

def minmax(data):
    minval = data[0]
    maxval = data[0]

    for val in data:
        if minval > val:
            minval = val
        if maxval < val:
            maxval = val
    
    return minval,maxval

data = list(map(int, input().split()))
ans = minmax(data)
print(type(ans))
print(ans)