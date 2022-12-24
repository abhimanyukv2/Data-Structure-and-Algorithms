'''Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax and the built-in sum function.'''

def comprehension(n):
    return sum([i*i for i in range(n) if i&1])

n = int(input())
ans = comprehension(n)
print(ans)