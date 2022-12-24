'''Demonstrate how to use Python’s list comprehension syntax to produce the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].'''

'''
0 = 1*0
2 = 1*2
6 = 2*3
12 = 3*4
20 = 4*5
30 = 5*6
42 = 6*7
56 = 7*8
72 = 8*9
90 = 9*10
'''

def comprehension(n):
    return [x*(x+1) for x in range(n)]

n = int(input())
print(comprehension(n))