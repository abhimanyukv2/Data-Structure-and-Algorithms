'''Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256].'''

def listComprehension(n):
    return [2**i for i in range(0,n+1)]

n = int(input())
ans = listComprehension(n)
print(ans)