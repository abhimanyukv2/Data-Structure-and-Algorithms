'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.'''

def sumOfSquare(n):
    ans = 0
    for i in range(n):
        ans = ans + (i*i)
    return ans

n = int(input())
ans = sumOfSquare(n)
print(ans)