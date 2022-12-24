'''Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n.'''

def sumSquareOdd(n):
    ans = 0
    for i in range(n):
        if i&1 == 1:
            ans += i**2
    return ans

n = int(input())
ans = sumSquareOdd(n)
print(ans)